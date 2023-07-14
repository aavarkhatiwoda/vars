from bs4 import BeautifulSoup
import requests
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}


def getMath(command):
	search = requests.get(f'https://www.desmos.com/scientific')
	soup = BeautifulSoup(search.text, 'html.parser')
	for i in soup:
		print(i)

getMath("5+5")