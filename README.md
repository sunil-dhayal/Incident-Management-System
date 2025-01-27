This project builds Incident Management System and explains it's features

# Dependencies

Python
django
djangorestframework
sqllite
phonenumbers
django-phonenumber-field
crispy_forms
crispy_bootstrap4

Could have more dependencies I might have missed, please consider installing

# Techstack

Django + sqllite

# Demo

Please see the png files inside project

# Settings.py

consider setting ALLOWED_HOSTS in settings.py

# Run

python manage.py runserver IP:Port  # 0.0.0.0:5555

# Features

Following are the rest endpoints exposed

## Admin

http://<IP>:<PORT>/admin/

Login using user: admin@admin.com and password admin@1234
or consider removing db and migration file and run python manage.py createsuperuser and set accordingly

This UI offers to see users and incidents and play with them

## User

http://<IP>:<PORT>/users/register/
Register your user

http://<IP>:<PORT>/users/login/
Login with user email

http://<IP>:<PORT>/users/profile/
Logined user profile

User portal has links to create and see incidents created by it

## incidents

http://<IP>:<PORT>/incidents/
List incidents

http://<IP>:<PORT>/incidents/create/
create incident

http://<IP>:<PORT>/incidents/<str:incident_id>/update/
update incident
