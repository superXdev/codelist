from django.shortcuts import render
from django.urls import reverse

import requests
from requests.compat import quote_plus 
from bs4 import BeautifulSoup
from . import models



CRAIGLIST_URL = 'https://newyork.craigslist.org/search/{}?query={}&sort={}&lang=en&cc=gb'
IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

def home(request):
	return render(request, 'base.html')

def about(request):
	return render(request, 'app/about.html')

def new_search(request):
	# get keyword search
	search = request.POST.get('search')
	# another option
	category = request.POST.get('category')
	sort = request.POST.get('filter')
	# getting the webpage
	url = CRAIGLIST_URL.format(category, quote_plus(search), sort)
	response = requests.get(url)
	# passing the source code
	soup = BeautifulSoup(response.text, features='html.parser')
	# extract all post
	post_lists = soup.find_all('li', {'class': 'result-row'})

	result_posts = []
	for post in post_lists:
		try:
			title = post.find(class_='result-title').text
			url = post.find('a').get('href')
			price = 'N/A'
			image_url = 'https://stickershop.line-scdn.net/stickershop/v1/product/1000415/LINEStorePC/main.png;compress=true'

			if post.find(class_='result-price'):
				price = post.find(class_='result-price').text

			if post.find(class_='result-image'):
				ids = post.find(class_='result-image').get('data-ids')
				image_url = ids.split(",")[0].split(":")[1]
				image_url = IMAGE_URL.format(image_url)

			result_posts.append((title, url, price, image_url))
		except:
			print('Error')

	data = {
		'search': search,
		'posts': result_posts,
	}
	return render(request, 'app/new_search.html', data)