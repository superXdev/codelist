from django.shortcuts import render

from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(request):
	return render(request, 'base.html')

def new_search(request):
	data = {
		'search': request.POST.get('search')
	}
	return render(request, 'app/new_search.html', data)