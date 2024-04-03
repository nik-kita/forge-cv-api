# some notes about specific usage in project:
* project has `models` module
* this module has public export of actual models (is using accross project)
* also has `versions` submodule so:
  * __each models's snapshot is saving in this module and forever exported to appropriate migration__
  * __it may be also exported to `models` module and from there reexported to project__
* so `models` works as a source of links to __actual for project__ models in `versions`

# Example
* suppose we generate new migration file with `1234` prefix
* in `database/models/versions` we create `user_1234.py` file with `User` model
* in migration file we import this model and write with it's help `up()`
* in `database/models/user` we also reexport this model
* ...
* we want to add new column ot `User` so +- repeat steps above:
  1. gen migration
  2. in `database/models/versions` create/extend/rewrite/copy => new `User` model
  3. use this model in migration
  4. change reexport in `database/models/user` to use actual new model
* so project will have updated model and migrations also are written with their help

## alembic usage:
* `alembic revision -m 'alter users'`
* `alembic downgrade`
* `alembic upgrade head`
