from bs4 import BeautifulSoup
import requests


headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}


def getWeather(location):

    location = location.replace(' ', '+')
    search = requests.get(f'https://www.google.com/search?client=firefox-b-1-d&q={location}', headers = headers)
    soup = BeautifulSoup(search.text, 'html.parser')
    try:
    	curtemp = str(soup.select("#wob_tm")[0].getText().strip())
    	datetime = str(soup.select('#wob_dts')[0].getText().strip())
    	forecast = str(soup.select('#wob_dc')[0].getText().strip()).lower()
    	st = f'As of {datetime}, it is {curtemp} °F, {str(int((int(curtemp)-32)*5/9))} °C with a {forecast} forecast.'
    	#st = 'As of ' + datetime + ', it is ' + curtemp + ' °F, ' + str(int((int(curtemp)-32)*5/9)) + ' °C with a ' + forecast + ' forecast.'
    	#print(st)
    	return st
    except:
    	return 'invalid'


    # CURRENT LOCATION x = soup.select('#EOlPnc')[0].getText().strip()
    #print(x)

    """
    x = soup.select('#main')[0].getText().strip()
    x = x[x.index('Weather') + 7 : x.index('More on weather.com')]
    x = x[:x.index('°F')+2] + ' ' + x[x.index('°F') + 2 : ]
    print(x[x.index('Weather')+7 : x.index('More on weather.com') ])
    """


#getWeather("weather in miami");

"""
'inv
	0].getText().strip()
      forecast = soup.select('#')[0].getText().strip()
      #temperature = (soup.select('#wob_tm')[0].
	0].getT I return 'temperatureay + degrees Celcius(andature)-32)*5/9)) + '
st.lowe
    orecast'
 except:
 urn 'try again, sir.'
 """
