# trainingsetbuilder
This project helps us build a training set for the Aztec tool classification project. Users can manually classify publications as either containing a new software tool or not.

```
#setup
pip install virtualenv
virtualenv --python=`which python` ~/.virtualenvs/django
source ~/.virtualenvs/django/bin/activate
pip install django

#launch
source ~/.virtualenvs/django/bin/activate
python manage.py runserver
```

Find a tool to classify on localhost:8000/classify/next

View database at localhost:8000/admin
