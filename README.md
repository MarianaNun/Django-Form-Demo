# django-form-demo

## Running Locally

```sh
$ git clone https://github.com/Arcangel617/django-form-demo.git
$ cd django-form-demo

$ python3 -m venv .venv
$ pip3 install -r requirements.txt

$ python manage.py migrate

$ python3 migrate.py runserver
```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

```sh
$ heroku login
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```

## Monitoring commands

`heroku ps` allows you to check the status of your application.

`heroku logs --tail` allows you to check all the activity in the server regarding your applcation.

## Troubleshooting

You might need to run `heroku config:set DISABLE_COLLECTSTATIC=1` in order to disable collectstatic

Also you might need add your heroku domain to `ALLOWED_HOSTS` at your `settings.py`.