# djangoProject
Try and Error Project for Django

## Before start
**Edit** `EMAIL_HOST_USER` `EMAIL_HOST_PASSWORD` in `djangoProject/settings.py`
#### Create new requirements
`pip freeze > requirements.txt`

## Setup for fresh start
#### Install requirements
`pip install -r requirements.txt`

The following two steps are summarized `makeMigrate.sh`
### Make new Migrations
`python manage.py makemigrations djangoProject`

### Migrate new migrations
`python manage.py migrate`

