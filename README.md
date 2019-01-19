# flask  migrate demo

> https://flask-migrate.readthedocs.io/en/latest/
> pip install Flask-Migrate

## Commands
### create db

``` sql
create test1;
use test1;
insert into `user` (name) values ('test1');
```

### run command below

```bash
flask db init
flask db migrate
flask db upgrade
# flask db downgrade
flask db --help
```

## Requirement

### Mysql

 - pip install pymysql
 
 ## TODO

  [x] flask web & flask migrate coexist
  [ ] dotenv
  [ ] BDD
