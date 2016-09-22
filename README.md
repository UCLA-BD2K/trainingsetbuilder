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

How to add a bunch of new publications to the database(example):
```python
from classify.models import Publication
import urllib2, json

journal = 'Bioinformatics (Oxford, England)'
count = 5000
query = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term="' + journal + '"[Journal]&retmode=json&retmax=' + str(count)

response = urllib2.urlopen(query).read()
data = json.loads(response)
idlist = data["esearchresult"]["idlist"]
for pm_id in idlist:
	p = Publication(pmid=pm_id, classification=-1)
	p.save()
```
