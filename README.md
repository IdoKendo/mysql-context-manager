# MySQL Context Manager

 > Work with MySQL based databases asynchronously, using a context manager.

[![PyPI version][pypi-image]][pypi-url]
[![PyPI downloads][downloads-image]][downloads-url]
[![Build status][build-image]][build-url]
[![Code coverage][coverage-image]][coverage-url]
[![Codacy Badge][codacy-image]][codacy-url]
[![Support Python versions][versions-image]][versions-url]

## Getting started

You can [get `mysql-context-manager` from PyPI](https://pypi.org/project/mysql-context-manager/),
which means you can install it with pip easily:

```bash
python -m pip install mysql-context-manager
```

## Example

```py
from mysql_context_manager import MysqlConnector

async with MysqlConnector(hostname="localhost") as conn:
    results = await conn.query("select username from users where is_bender = 1 order by username asc;")
assert results[0]["username"] == "Aang"
assert results[1]["username"] == "Katara"
assert results[2]["username"] == "Toph"
```

## Example using SQLAlchemy

```py
from mysql_context_manager import MysqlConnector
import sqlalchemy
from sqlalchemy.dialects import mysql

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("user_id", mysql.INTEGER(), autoincrement=True, nullable=False),
    sqlalchemy.Column("username", mysql.VARCHAR(length=128), nullable=False),
    sqlalchemy.Column("is_bender", mysql.SMALLINT(), autoincrement=False, nullable=True),
    sqlalchemy.PrimaryKeyConstraint("user_id"),
    mysql_default_charset="utf8mb4",
    mysql_engine="InnoDB",
)

async with MysqlConnector(hostname="localhost") as conn:
    results = await conn.query(users.select().where(users.c.username == "Aang"))
assert results[0]["username"] == "Aang"
assert results[0]["is_bender"] == 1
```

## Changelog

Refer to the [CHANGELOG.rst](CHANGELOG.rst) file.

<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/mysql-context-manager
[pypi-url]: https://pypi.org/project/mysql-context-manager/
[downloads-image]: https://img.shields.io/pypi/dm/mysql-context-manager.svg
[downloads-url]: https://pypistats.org/packages/mysql-context-manager
[build-image]: https://github.com/idokendo/mysql-context-manager/actions/workflows/build.yaml/badge.svg
[build-url]: https://github.com/idokendo/mysql-context-manager/actions/workflows/build.yaml
[coverage-image]: https://codecov.io/gh/idokendo/mysql-context-manager/branch/main/graph/badge.svg
[coverage-url]: https://codecov.io/gh/idokendo/mysql-context-manager
[versions-image]: https://img.shields.io/pypi/pyversions/mysql-context-manager
[versions-url]: https://pypi.org/project/mysql-context-manager/
[codacy-image]: https://app.codacy.com/project/badge/Grade/59b037e21c4e4c6ea5a51f4a693dc267
[codacy-url]: https://www.codacy.com/gh/IdoKendo/mysql-context-manager/dashboard
