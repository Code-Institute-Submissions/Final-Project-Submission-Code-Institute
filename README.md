[![Build Status](https://travis-ci.org/coderguider/Final-Project-Submission-Code-Institute.svg?branch=master)](https://travis-ci.org/coderguider/Final-Project-Submission-Code-Institute)

# CREATE AN ISSUE TRACKER

## Brief

Create a web application that allows users to report bugs and suggest features.
[View Site](https://unicornattractor-issuetracker.herokuapp.com/)

## How to Use Web Application

* Once you visit the site you need to register an account.
* Once registered you will be able to add your own bugs and features
* You can view them from your profile
* In order to Vote for features you will have to pay a fee of €10
* This is done with Stripes API - DO NOT USE YOUR OWN CREDIT CARD NUMBER - USE 4242 4242 4242 4242 - THIS IS FOR TESTING PURPOSES ONLY
* The Admin will have their own protocol to view bugs and features posted, as well as mark their progress

## Technologies

1. Django
2. HTML
3. CSS
4. Bootstrap
5. JQuery
6. Python
7. Stripe
8. Jinja2

## Features

1. User Registration and Login
2. Users have the ability to create their own bug reports
3. Users can create features as suggestions to the community
4. Users have the ability to "Vote" on those features
5. Voting on features creates a €10 ammount in their carts
6. Stripe will handle the payment
7. Admin login can view, delete and edit posts.
8. Admin can mark bugs and features as "To do", "Doing" and "Done"


## Testing
Manual testing was undertaken for this application and satisfactorily passed. Tests were conducted as follows: 
1. Unit testing - Tested small chunks of the code as I progressed to ensure the code is functioning
2. Integration testing - Tested combinations of units to ensure new code doesn't interfere with existing code
3. Acceptance testing — Tested the application in sevreal different browsers and devices to analyze the performance of the entire application.
4. Code which was credited, was tested as the example given, then modified for desired outcome
5. Test.py files were created to ensure code was opperating


## Design
Built primarily off the mini project example as the basic framework. Website layout was implemented with Bootstrap and custom styled.

## Deployment

Create a django project:
$ django-admin startproject UnicornAttractor

Make the migrations:
$ python3 manage.py makemigrations

Run migrate:
$ python3 manage.py migrate

Run migrations on Heroku:
$ heroku run python3 manage.py migrate

Create a superuser:
$ python manage.py createsuperuser

Install requirements with pip:
$ pip install -r requirements.txt

Run the python file:
$ python3 manage.py runserver $IP:$PORT


## Credits

**Conor Guider** - This project was completed as part of Code Institute's Full Stack Web Development course.

### Media
* PixelBay for the landing-page
* Styling was from Bootstrap

### Acknowledgments
* Resources - Codedrops, Stackoverflow, Bootstrap.
