# pylint: disable=C0114,C0115,R0913
from __future__ import annotations

__version__ = "0.2.0"

import contextlib
import json
from json import JSONDecodeError
from typing import Any

import databases


class MysqlConnector:
    def __init__(
        self,
        hostname: str,
        username: str = "root",
        password: str | None = None,
        schema: str | None = None,
        port: int = 3306,
    ):
        """Async connector object for a MySQL database

        Args:
            hostname (str): Hostname of the database
            username (str, optional): Username. Defaults to "root".
            password (str | None, optional): Password, if exists. Defaults to None.
            schema (str | None, optional): Schema, if required. Defaults to None.
            port (int, optional): Port. Defaults to 3306.
        """
        credentials = username if password is None else f"{username}:{password}"
        if schema is None:
            schema = ""
        self.connection_string = f"mysql://{credentials}@{hostname}:{port}/{schema}"
        self.connection: databases.Database | None = None
        self.engine = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

    def __await__(self):  # pragma: no cover
        return self.__aenter__().__await__()

    async def disconnect(self) -> None:
        """If connection is established, disconnects"""
        if self.connection is not None:
            await self.connection.disconnect()

    async def connect(self) -> None:
        """Establishes the connection to the database"""
        self.connection = databases.Database(self.connection_string)
        if self.connection is not None:
            await self.connection.connect()

    async def query(self, sql_query: str, **kwargs) -> list[dict[str, Any]]:
        """Queries the database

        Args:
            sql_query (str): SQL query, with placeholders as :placeholder

        Returns:
            list[dict[str, Any]]: List of rows represented in dictioary format

        Raises:
            ConnectionError: in case of method call before running connect()

        Examples:
            >>> query = "select name, elem from users where team = :team limit 2;"
            >>> async with MysqlConnector(hostname="localhost") as conn:
            >>>    print(await conn.query(query, team="Team Avatar"))
            [{"name": "Katara", "elem": "water"}, {"name": "Toph", "elem": "earth"}]

        """
        if self.connection is None:
            raise ConnectionError("No active connection")
        records = await self.connection.fetch_all(query=sql_query, values=kwargs)
        result = [dict(i) for i in records]
        for res in result:
            for key, val in res.items():
                with contextlib.suppress(JSONDecodeError, TypeError):
                    res[key] = json.loads(val)
        return result

    async def execute(self, sql_query: str, **kwargs) -> None:
        """Executes and commits an SQL query to the database

        Args:
            sql_query (str): SQL query, with placeholders as :placeholder

        Raises:
            ConnectionError: in case of method call before running connect()

        Examples:
            >>> query = "update users set name = :name where user_id = :user_id;"
            >>> async with MysqlConnector(hostname="localhost") as conn:
            >>>    await conn.query(query, name="Truth", user_id=42)
        """
        if self.connection is None:
            raise ConnectionError("No active connection")
        await self.connection.execute(query=sql_query, values=kwargs)
