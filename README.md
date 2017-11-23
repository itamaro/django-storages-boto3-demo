# Django Storages S3Boto3 Demo

A demo Django app using django-storages with S3Boto3 backend to display images from S3 bucket, uploaded from admin interface.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:itamaro/django-storages-boto3-demo.git
$ cd django-storages-boto3-demo

$ pipenv install

$ createdb django_storages_boto3

$ pipenv run python manage.py migrate
$ pipenv run python manage.py collectstatic

$ pipenv run heroku local -p 8000 web
```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
