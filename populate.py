from classify.models import Publication
import json

journal = 'PLoS computational biology'

response = open('response.json', 'r')
data = json.loads(response.read())
idlist = data["esearchresult"]["idlist"]
for pm_id in idlist:
    p = Publication(pmid=pm_id, classification=-1)
    p.journal = journal
    p.save()
