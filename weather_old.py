from bs4 import BeautifulSoup
import requests
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def giveWeather(location):
	location = location.replace(' ', '+')
	search = requests.get(f'https://www.google.com/search?client=firefox-b-1-d&q={location}', headers = headers)
    #res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    #res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    #res = requests.get(f'https://www.google.com/search?client=firefox-b-1-d&q={city}', headers=headers)
    #res = requests.get(f'https://www.google.com/search?client=firefox-b-1-d&q={city}', headers=headers)
    #res = requests.get(f'https://www.google.com/search?client=firefox-b-1-d&q={city}', headers=headers)
	#print("Searching...\n")
	soup = BeautifulSoup(search.text, 'html.parser')
	#location = soup.select('#wob_loc')[0].getText().strip()
	#time = soup.select('#wob_dts')[0].getText().strip()
	info = soup.select('#wob_dc')[0].getText().strip()
	temp = soup.select('#wob_tm')[0].getText().strip()
	#print(location)
	#print(time)
	#print(info)
	print(temp + ' degrees Celcius and ' + info.lower())


#city = input('')
#city = city + ' weather'
giveWeather(input())



"""
from bs4 import BeautifulSoup
import requests
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}


def getWeather(location):

    location = location.replace(' ', '+')
    search = requests.get(f'https://www.google.com/search?client=firefox-b-1-d&q={location}', headers = headers)
    soup = BeautifulSoup(search.text, 'html.parser')


    curtemp = str(soup.select("#wob_tm")[0].getText().strip())
    datetime = str(soup.select('#wob_dts')[0].getText().strip()).lower()
    forecast = str(soup.select('#wob_dc')[0].getText().strip()).lower()
	
    #print(soup.find("span", attrs={"id": "wob_dc"}))
    st = 'As of ' + datetime + ', it is ' + curtemp + ' °F, ' + str(int((int(curtemp)-32)*5/9)) + ' °C with a ' + forecast + ' forecast.'
    print(st)
    return st
"""
