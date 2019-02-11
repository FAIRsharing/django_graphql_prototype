Prototype Appliction
--------------------

This is designed to test out various components we might use for a redesign of FAIRsharing to use Python 3, Django 2 
and GraphQL rather than REST. To set this up:

1. Create a virtualenv with Python 3 (e.g. `virtualenv --python=python3 prototype`) and activate it.
2. Install the various packages with `pip install -r requirements.txt`.
3. Create a postgres database, put the configuration in secrets.py, and then run `manage.py migrate`. You may also
need to run `makemigrations` and `migrate` again to add the model(s) in models.py.
4. Create some models for testing with `python manage.py loadtestdata fairsharing.FairsharingRecord:5`.
5. Create an admin user with `manage.py createsuperuser`.


Fun with GraphQL
----------------

Here's a tutorial:

http://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/

And another:

https://github.com/mbrochh/django-graphql-apollo-react-demo

Stuff To Do
-----------

Lots, for example:

1. Proper user authorisation.
2. Fix this so it actually works (e.g. tests).
