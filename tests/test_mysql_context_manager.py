import pytest
from mysql_context_manager import __version__
from mysql_context_manager import MysqlConnector


@pytest.fixture()
def mock_db(mocker):
    mocker.patch("databases.Database.connect", return_value=None)
    mocker.patch("databases.Database.disconnect", return_value=None)
    mocker.patch(
        "databases.Database.fetch_all",
        return_value=[
            [("username", "Aang")],
        ],
    )
    mocker.patch("databases.Database.execute", return_value=None)


def test_version():
    assert __version__ == "0.1.2"


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
        result = await conn.query("select username from users;")
    assert result[0]["username"] == "Aang"


@pytest.mark.asyncio
async def test_execute(mock_db):
    connector = MysqlConnector(hostname="localhost", schema="team_avatar")
    async with connector as conn:
        await conn.execute("update users set avatar_state = 1 where username = :username;", username="Aang")
