
2022-08-02
==========

Added
-----

- Run tox on windows in GH actions.

Changed
-------

- Using pytest-cov instead of bare coverage.
- Lowered minimum python version to 3.8

2022-07-31
==========

Added
-----

- Added example using SQLAlchemy.
- Added automatic deploy action to PyPI.

2022-07-28
==========

Removed
-------

- Redundant SQLAlchemy engine initialization

Added
-----

- Unit testing and code coverage
- Tox testing
- Docstring

Changed
-------

- Lowered minimum python version to 3.9

2022-07-28
==========

Added
-----

- Initial implementation of MysqlConnector to allow asynchronously context manage MySQL connection.
