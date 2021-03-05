# django-vue-project

# Backend Technical details

Here are steps described to run the application locally.

## Creating virtual environment

`python -m venv .venv` -- first time when you start working on the project or
`python3 -m venv .venv` -- first time when you start working on the project when python3 is not your default python version.

## Activate

`source .venv/bin/activate`-- each time when you start working on the project, or when it's deactivated

To deactivate the environment use the command below:
`deactivate`

## Upgrade package manager

`pip install --upgrade pip` - first time when you install the environment
`pip install wheel setuptools pip-tools` - first time when you install the environment

## Install packages

`pip install -r requirements.txt` - each time when new package is installed by any team member

- list packages installed on the environment `pip freeze`
- dump all packages to a text file `pip freeze > requirements.txt`

## Run django from /backend folder

- `python manage.py makemigrations` - first time needed or when new models are added
- `python manage.py migrate` - first time needed or when new models are added
- `python manage.py createsuperuser` - admin, ,admin, admin, yes
- `python manage.py runserver` - to run the server
- `python manage.py test api` - to run test

# Frontend Technical details

## Install dependencies 

From /frontend folder run
- `npm install`

## Serve development server

From /frontend folder run

-  `num run serve`

Also add Vue origin at `CORS_ALLOWED_ORIGINS = []` in `settings.py`
and Django Rest Api endpoint in env variable `VUE_APP_BASE_RISK_TYPE_API_URL`

# Running with Docker

In main project folder run `docker-compose build` and `docker-compose up` to start Django and Vue apps.

# Documentation

Read Documentation.pdf in main project folder
