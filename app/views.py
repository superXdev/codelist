from django.shortcuts import render

import requests
from requests.compat import quote_plus 
from bs4 import BeautifulSoup
from . import models

CRAIGLIST_URL = 'https://newyork.craiglist.org/search/?query={}'

def home(request):
	return render(request, 'base.html')

def new_search(request):
	search = request.POST.get('search')
	url = CRAIGLIST_URL.format(quote_plus(search))
	# response = requests.get(url)
	r = ('c', 'a', 'd')
	data = {
		'search': r
	}
	return render(request, 'app/new_search.html', data)