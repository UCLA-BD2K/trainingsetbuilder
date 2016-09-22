from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

# Create your views here.
from django.http import HttpResponse
import urllib2, json, re, random

from .models import Publication

def index(request):
	return HttpResponse("You're at the classify index.")

def titleDoiFromPmid(pmid):
	response =  urllib2.urlopen("http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&rettype=abstract&id=" + str(pmid)).read()
	data = json.loads(response)
	title = data["result"][pmid]["title"]
	doi = "none"
	for id in data["result"][pmid]["articleids"]:
		if id["idtype"] == "doi":
			doi = id["value"]

	return str(title), str(doi)

def bodyFromAbstract(abstract):
    result = re.search(r"Author information: \n((.+)\n)+\n(((.+)\n)+)", abstract, re.M)
    return result.group(3)

def pubmedQuery(pmid):
    return urllib2.urlopen("http://www.ncbi.nlm.nih.gov/pubmed/" + str(pmid) + "?report=abstract&format=text").read()

def detail(request, pmid):
	title, doi = titleDoiFromPmid(pmid)
	abstract = str(bodyFromAbstract(pubmedQuery(pmid)))
	link = "http://doi.org/" + doi
	return render(request, 'classify/detail.html', {'title': title, 'abstract': abstract, 'link': link})

def tool(request, pmid):
	publication = get_object_or_404(Publication, pk=pmid)
	publication.classification = 1
	publication.save()
	return redirect("/classify/next/")

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
