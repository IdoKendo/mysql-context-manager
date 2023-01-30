import pytest
from mysql_context_manager import MysqlConnector, __version__


def test_version():
    assert __version__ == "0.1.6"


def test_connection_string():
    connector = MysqlConnector(hostname="localhost")
    assert connector.connection_string == "mysql://root@localhost:3306/"


def test_connection_string_with_schema_name():
    connector = MysqlConnector(hostname="localhost", schema="team_avatar")
    assert connector.connection_string == "mysql://root@localhost:3306/team_avatar"


@pytest.mark.asyncio
async def test_false_disconnect():
    connector = MysqlConnector(hostname="localhost")
    assert connector.connection is None
    await connector.disconnect()
    assert connector.connection is None


@pytest.mark.asyncio
async def test_query(mock_db):
    connector = MysqlConnector(hostname="localhost", schema="team_avatar")
    async with connector as conn:
        result = await conn.query("select name from users;")
    assert result[0]["name"] == "Aang"


@pytest.mark.asyncio
async def test_execute(mock_db):
    connector = MysqlConnector(hostname="localhost", schema="team_avatar")
    async with connector as conn:
        await conn.execute(
            "update users set avatar_state = 1 where name = :name;",
            name="Aang",
        )


@pytest.mark.asyncio
async def test_query_without_connection(mock_db):
    connector = MysqlConnector(hostname="localhost", schema="team_avatar")
    with pytest.raises(ConnectionError):
        await connector.query("select name from users;")


@pytest.mark.asyncio
async def test_execute_without_connection(mock_db):
    connector = MysqlConnector(hostname="localhost", schema="team_avatar")
    with pytest.raises(ConnectionError):
        await connector.execute(
            "update users set avatar_state = 1 where name = :name;",
            name="Aang",
        )
