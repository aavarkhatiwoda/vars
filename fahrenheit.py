from bs4 import BeautifulSoup
import requests

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def getFahrenheit(celciusInput):

    location = location.replace(' ', '+')
    #search = requests.get(f'https://www.google.com/search?client=firefox-b-1-d&q={celciusInput}', headers = headers)
    search = requests.get(f'https://www.google.com/search?q={location}&oq={location}&aqs=chrome.0.69i59j0i512l9.1098j1j7&sourceid=chrome&ie=UTF-8', headers = headers)
    soup = BeautifulSoup(search.text, 'html.parser')

    try:
        forecast = soup.select('#wob_dc')[0].getText().strip()
        #temperature = (soup.select('#wob_tm')[0].getText().strip() - 32)*5.0/9
        temperature = soup.select('#wob_tm')[0].getText().strip()
        return "It is " + temperature + ' degrees Fahrenheit and ' + forecast.lower()
    except:
        return 'try again, sir.'
