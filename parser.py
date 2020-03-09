import requests
from bs4 import BeautifulSoup
import re
import json
from jsoncomment import JsonComment

def get_html(url):
	user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/72.0.3626.81 Safari/537.36'
	r = requests.get(url, headers={'User-Agent': user_agent}) 
	if r.ok:
		return r.text 
	else:
		exp = HttpException() 
		exp.status_code = r.status_code 
		raise exp


def get_page_data(html):
	data_list = []
	soup = BeautifulSoup(html, 'html.parser')
	script  = soup.find_all('script', type='text/javascript')[2].string
	f = open("first.json", "w")
	script = script.replace("window.insider_object", "\"window.insider_object\"")
	f.write("{" + script.replace("=", ":").replace("'", "\"") + "}")
	f.close()
	with open("first.json") as data_file:    
		parser = JsonComment(json)
		data = parser.load(data_file)
		print(data["window.insider_object"]["listing"]["items"])

def get_parsed_json():
	page_size = 10
	page_item_size = 20

	category = "smartfoniy"
	city = "almaty"
	
	for page in range(1, page_size):
		print(page)
		url = "https://www.sulpak.kz/f/{}/{}/~/~/~/PopularityDesc/default/~/{}/{}".format(category, city, page, page_item_size)
		print(url)
		get_page_data(get_html(url))

get_parsed_json()
