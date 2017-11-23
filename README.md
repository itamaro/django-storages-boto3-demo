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
$ pipenv run python manage.py createsuperuser
$ pipenv run python manage.py collectstatic
$ cat <<EOF >.env
AWS_ACCESS_KEY="<Access-Key>"
AWS_SECRET_KEY="<Secret-Key>"
AWS_S3_BUCKET="S3-Bucket"
EOF

$ pipenv run heroku local -p 8000 web
```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku config:set \
    AWS_ACCESS_KEY="<Access-Key>" \
    AWS_SECRET_KEY="<Secret-Key>" \
    AWS_S3_BUCKET="S3-Bucket"
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Using the Demo

Using the admin interface (with the credentials of the superuser created), create "UploadedImage" records, uploading images from your local machine, then view the images ob the home page of the app.

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
