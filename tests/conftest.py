import pytest


@pytest.fixture
def _mock_db(mocker):
    mocker.patch("databases.Database.connect", return_value=None)
    mocker.patch("databases.Database.disconnect", return_value=None)
    mocker.patch(
        "databases.Database.fetch_all",
        return_value=[
            [("name", "Aang")],
        ],
    )
    mocker.patch("databases.Database.execute", return_value=None)
