# Incident-Management-System
A web Application to create users and allow them to create incident tickets and play with it.

# Here is the problem statement it tries to solve

You have to create a REST API for an incident management system.

## Development Environment

Ubuntu (Version 18 & above), Development Language Python 3.8 and above, Django and Database MySQL.

## 1. Front-End development: 
The key functionalities are:
  a. Registration Page for the user
  b. Login Page
  c. Forgot Password
  d. Create/view/edit- Incident- Use your own UI based on the inputs given below in the backend section.

## 2. Back-End Development:
This is implemented using Python/Django Rest Framework. It allows a user to log in and create incidents. It is using sqlite but soon will be replace with MySQL. The Key functionalities for the entire solution are:
  a. System should allow you to create multiple users.
  b. Each User should be unique and should have the following details. You need to use any library wherein the moment one enters the pin code, it should auto-select the City and Country,
    i. User Name
    ii. User Email ID
    iii. User Phone Number
    iv. User Address, Pin code
    v. City and Country.
  c. System should allow any user to create multiple incidents.
  d. Each user can create multiple incidents.
  e. Each Incident to have the following
    i. Fields to identify Enterprise or Government
    ii. Details of the person reporting the incident
    iii. Ensure that if the person entering the details exists, auto-fill previous information
    iv. Auto-generate Incident ID and ensure that the format for the Incident ID should be the following format- RMG + Random 5-digit number+ Current year (2022) e.g. RMG345712022
    v. You need to ensure that each incident number should be unique. So implement methods to check the uniqueness of the Incident.
    vi. The incidents should have the following details-
      a.Reporter name (Name of the user who logs in and creates the incident)
      b. Incident details (text field) Should be editable
      c.Incident Reported date and time
      d. Priority (Dropdown with values High, Medium, Low) Should be editable
      e.Incident status (Open, In progress, Closed) Should be editable
      f. Limitations
        i. A User should be allowed to view and edit the incidents created by them only.
        ii. No user should be able to view other users’ incidents.
        iii. Any Incident which has the state = closed, should not be editable.
        iv. There should be a provision to search the incident using the incident ID.

# Developer Guide

## Dependencies

Python
django
djangorestframework
sqllite
phonenumbers
django-phonenumber-field
crispy_forms
crispy_bootstrap4

Could have more dependencies I might have missed, please consider installing, will add docker support soon...

## Techstack

Django + sqllite

## Demo

Please see the png files inside project

## Settings.py

Consider setting ALLOWED_HOSTS in settings.py

## Run

python manage.py runserver IP:Port  # 0.0.0.0:5555

## Features

Following are the rest endpoints exposed

### Admin

http://<IP>:<PORT>/admin/

Login using user: admin@admin.com and password admin@1234
or consider removing db and migration file and run python manage.py createsuperuser and set accordingly

This UI offers to see users and incidents and play with them

### User

http://<IP>:<PORT>/users/register/
Register your user

http://<IP>:<PORT>/users/login/
Login with user email

http://<IP>:<PORT>/users/profile/
Logined user profile

User portal has links to create and see incidents created by it

### incidents

http://<IP>:<PORT>/incidents/
List incidents

http://<IP>:<PORT>/incidents/create/
create incident

http://<IP>:<PORT>/incidents/<str:incident_id>/update/
update incident
