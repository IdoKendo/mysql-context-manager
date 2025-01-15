
2025-01-15
==========

Added
-----

- Official support to Python 3.13.
- Experimental support to Python 3.14-alpha.

Removed
-------

- Removed support for Python 3.8.

Security
--------

- Updated minimum version for most dependencies.

2023-10-18
==========

Added
-----

- Official support to Python 3.12.
- Experimental support to Python 3.13-alpha.

Security
--------

- Updated minimum version for many dependencies.

2023-05-24
==========

Added
-----

- Added mypy type checker

- Added support for python 3.12-dev

Changed
-------

- Changed linting to ruff

- query() and execute() will raise ConnectionError in case they are run without active connection.

2022-12-13
==========

Security
--------

- Update dependencies' versions.

2022-10-25
==========

Added
-----

- Support for Python 3.11.

Changed
-------

- Tidied up the tox and GH actions stages
- Updated pyproject.toml to new poetry group depdendencies
- Updated depdendencies

2022-08-03
==========

Fixed
-----

- Run tox on python 3.8 in GH actions.
- Coverage image URL was broken.

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
