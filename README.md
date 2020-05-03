# Heavyweight

A Flask starter application with Auth, logging, db and CI/CD covered.

## The stack

  - Language: Python 3.8+
  - Application Framework: [Flask](https://palletsprojects.com/p/flask/)
  - Application Server: [uWSGI](https://uwsgi-docs.readthedocs.io/)
  - Web Server: [NGINX](https://www.nginx.com/)
  - Database: PostgreSQL 

The following libraries will be used for building the application.

  - API Endpoints: [Flask-Classful](http://flask-classful.teracy.org/)
  - ORM: [Flask-SQLAlchemy (SQLAlchemy)](https://flask-sqlalchemy.palletsprojects.com/)
  - DB Migrations: [Flask-Migrate (Alembic)](https://flask-migrate.readthedocs.io/en/latest/)
  - Serialization: [Marshmallow](https://marshmallow.readthedocs.io/)
  - Testing: [pytest](https://docs.pytest.org/en/latest/)

## Application structure

```
heavyweight
│
│  flask/
│  │
│  │ app/
│  │ │ auth/
│  │ │ status/
│  │ │ ...
│  │ │ ...
│  │ └───────
│  │ config/
│  │ │ local
│  │ │ prod
│  │ │ ...
│  │ └───────
│  │ migrations/
│  │ tests/
│  │ │ unit/
│  │ │ integration/
│  │ │ ...
│  │ └───────
│  │ requirements.txt
│  │ Dockerfile
│  │ entrypoint.sh
│  │ setup.cfg
│  └────────────────────────
│  nginx/
│  Postgresql/
│  entrypoint.sh
│  requirements.txt
│  docker-compose.yml
└────────────────────────
```

## Development setup

1. System requirements

   - Docker desktop
   - Python 3.8

2. Install required packages

  ```bash
  # create virtual env
  cd flask/
  python3 -m venv env

  # Activate the environment
  source ./env/bin/activate

  # Install packages
  pip3 install -r requirements.txt
  ```


## TODO

1. Modularize various components
2. Auth, Logging and DB should be configured
