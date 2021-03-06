from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

# Create your views here.
from django.http import HttpResponse
import urllib2, json, re, random

from .models import Publication

def index(request):
	total = len(Publication.objects.all())
	unclassified = len(get_list_or_404(Publication, classification=-1))
	tools = len(get_list_or_404(Publication, classification=1))
	nottools = len(get_list_or_404(Publication, classification=0))
	ambiguous = len(get_list_or_404(Publication, classification=2))
	return render(request, 'classify/summary.html', {'total': total, 'unclassified': unclassified, 'tools': tools, 'nottools': nottools, 'ambiguous': ambiguous})

def titleDoiFromPmid(pmid):
	response =  urllib2.urlopen("http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&rettype=abstract&id=" + str(pmid)).read()
	data = json.loads(response)
	title = data["result"][pmid]["title"]
	doi = "none"
	for id in data["result"][pmid]["articleids"]:
		if id["idtype"] == "doi":
			doi = id["value"]
	try:
		return str(title), str(doi)
	except:
		return title, str(doi)

def bodyFromAbstract(abstract):
    result = re.search(r"Author information: \n((.+)\n)+\n(((.+)\n)+)", abstract, re.M)
    try:
        return result.group(3)
    except: return abstract

def pubmedQuery(pmid):
    return urllib2.urlopen("http://www.ncbi.nlm.nih.gov/pubmed/" + str(pmid) + "?report=abstract&format=text").read()

def detail(request, pmid):
	title, doi = titleDoiFromPmid(pmid)
	abstract = str(bodyFromAbstract(pubmedQuery(pmid)))
	link = "http://doi.org/" + doi
	return render(request, 'classify/detail.html', {'title': title, 'abstract': abstract, 'link': link, 'pmid': pmid})

def tool(request, pmid):
	publication = get_object_or_404(Publication, pk=pmid)
	publication.classification = 1
	publication.save()
	return redirect("/classify/next/")

def data(request):
	pubs = get_list_or_404(Publication)

	tools = []
	not_tools = []
	ambiguous = []

	for p in pubs:
		publication = {}
		publication["pmid"] = p.pmid
		publication["journal"] = p.journal
		publication["fulltextviewed"] = p.fulltextviewed
		if p.toolname != "unknown":
			publication["toolname"] = p.toolname
		if p.classification == 0:
			not_tools.append(publication)
		if p.classification == 1:
			tools.append(publication)
		if p.classification == 2:
			ambiguous.append(publication)

	data = { "tools":tools, "not tools":not_tools, "ambiguous":ambiguous }

	return HttpResponse(json.dumps(data))

def nott(request, pmid):
	publication = get_object_or_404(Publication, pk=pmid)
	publication.classification = 0
	publication.save()
	return redirect("/classify/next/")

def ambiguous(request, pmid):
	publication = get_object_or_404(Publication, pk=pmid)
	publication.classification = 2
	publication.save()
	return redirect("/classify/next/")

def skip(request, pmid):
	return redirect("/classify/next/")

def next(request):
	next_pub = random.choice(get_list_or_404(Publication, classification=-1))
	return redirect("/classify/" + next_pub.pmid)
	
def fulltextviewed(request, pmid):
	publication = get_object_or_404(Publication, pk=pmid)
	publication.fulltextviewed = 1
	publication.save()
	return skip(request, pmid)

def settoolname(request, pmid, toolname):
	publication = get_object_or_404(Publication, pk=pmid)
	publication.toolname = toolname
	publication.save()
	return skip(request, pmid)
