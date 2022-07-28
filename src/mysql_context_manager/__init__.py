from __future__ import annotations

__version__ = "0.1.0"

import json
from json import JSONDecodeError
from typing import Any

import sqlalchemy
from databases import Database

metadata = sqlalchemy.MetaData()


class MysqlConnector:
    def __init__(self, hostname: str, username: str = "root", password: str | None = None, schema: str | None = None, port: int = 3306):
        credentials = username if password is None else f"{username}:{password}"
        if schema is None:
            schema = ""
        self.connection_string = f"mysql://{credentials}@{hostname}:{port}/{schema}"
        self.connection = None
        self.engine = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

    def __await__(self):
        return self.__aenter__().__await__()

    async def disconnect(self) -> None:
        if self.connection is not None:
            await self.connection.disconnect()

    async def connect(self) -> None:
        self.connection = Database(self.connection_string)
        self.engine = sqlalchemy.create_engine(f"mysql+py{self.connection_string}")
        metadata.create_all(self.engine)

        await self.connection.connect()

    async def query(self, sql_query: str, **kwargs) -> list[dict[str, Any]]:
        result = await self.connection.fetch_all(query=sql_query, values=kwargs)
        result = [dict(i) for i in result]
        for res in result:
            for key, val in res.items():
                try:
                    res[key] = json.loads(val)
                except (JSONDecodeError, TypeError):
                    pass
        return result

    async def execute(self, sql_query: str, **kwargs) -> None:
        await self.connection.execute(query=sql_query, values=kwargs)
