# Events ETL (a map-for-change racket)

Start of ETL for all events for progressive applications.


# Setting up Local Heroku
The following is based on the [Heroku Python Getting Started Guide](https://devcenter.heroku.com/articles/getting-started-with-python#run-the-app-locally)

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

# Setting Up ETL

## Buckets 

Setup buckets in `etl/peoplepower/main.py`

## Documentation

Checkout `http://peoplepower.actionkit.com/rest/v1` for more info

## ENV VARS 


| key | description |
|--- |--- |
| `PEOPLEPOWER_LAUNCH_URL` | API for the People Power LAUNCH campaign. Preface it with <username>:<password> |
| `PEOPLEPOWER_ACTION_URL` | API Endpoint for the People Power ACTION campaign |
| `AWS_ACCESS_KEY_ID` | AWS Access Key for the respective AWS |
| `AWS_SECRET_ACCESS_KEY` | AWS Secret Key |
| `AWS_HOST` | AWS HOST |
