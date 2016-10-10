from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse
import urllib2, json, re, random

from .models import Sentence

@csrf_exempt
def index(request):
	t = request.POST.get("sentence", "")
	a = request.POST.get("isAvailable", "") == u'true'
	s = Sentence(text=t, positive=a)
	s.save()
	return HttpResponse("Recieved!")
