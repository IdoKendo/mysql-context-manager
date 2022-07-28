# MySQL Context Manager

Work with MySQL based databases asynchronously, using a context manager.


## Getting started

You can [get `mysql-context-manager` from PyPI](https://pypi.org/project/mysql-context-manager/),
which means you can install it with pip easily:

```bash
python -m pip install mysql-context-manager
```

## Example

```py
from mysql_context_manager import MySqlConnector

async with MySqlConnector(hostname="localhost") as conn:
    results = await conn.query("select username from users where is_bender = 1 order by username asc;")
assert results[0]["username"] == "Aang"
assert results[1]["username"] == "Katara"
assert results[2]["username"] == "Toph"
```
