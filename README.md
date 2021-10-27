# djangoProject
Try and Error Project for Django

## Before start
**Edit** `EMAIL_HOST_USER` `EMAIL_HOST_PASSWORD` in `djangoProject/settings.py`
#### Create new requirements
`pip freeze > requirements.txt`

## Setup for fresh start

#### Install requirements
`pip install -r requirements.txt`

### Create new super user
`python manage.py createsuperuser`

The following two steps are summarized `makeMigrate`.sh (for linux) or .bat (for windows)

### Make new Migrations
`python manage.py makemigrations djangoProject`

### Migrate new migrations
`python manage.py migrate`

