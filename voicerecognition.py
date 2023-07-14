# importing speech recognition package from google api
import speech_recognition as sr
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open fipisudples
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
from Weather import *
from Synonyms import *
from datetime import datetime


functions = {
			'getWeather':getWeather,
			'getSynonyms':getSynonyms
			}


num = 1
def speak(output):
	global num
	num += 1
	print(output)
	toSpeak = gTTS(text = output, lang='en', tld='co.uk')
	file = str(num) + ".mp3"
	toSpeak.save(file)

	playsound.playsound(file, True)
	os.remove(file)


def getAudio():
	rObject = sr.Recognizer()
	audio = ''
	with sr.Microphone() as source:
		audio = rObject.listen(source, phrase_time_limit = 10)
	try:
		command = rObject.recognize_google(audio, language ='en-US')
		print(command)
		return command
	except:
		return ''


if __name__ == "__main__":

	# Google voice recognition does not adequately recognize the name 'Vars'
	name = 'jarvis'
	
	while True:
		command = getAudio().lower()

		if name in command:

			if 'wrap it up' in command or 'close up shop' in command:
				speak('See you tomorrow, sir.')
				exit(0)

			elif 'you there' in command:
				speak('At your service, sir')

			elif 'my name' in command:
				speak('Sir, please don\'t assume I am that low of an assistant to not know your name.')
				
			elif 'open ' in command or 'go to ' in command:
				command = command[len(name)+1:]
				search = requests.get(f'https://www.google.com/search?client=firefox-b-1-d&q={command}', headers = headers)
				soup = BeautifulSoup(search.text, 'html.parser')

				try:
					link = str(soup.find_all('a', href=True)[10]['href'])
					os.system(f'open {link}')

				except:
					print('invalid')

			elif 'weather' in command or 'temperature' in command or 'forecast' in command or 'hot' in command or 'cold' in command:
				command = command[len(name)+1:]
				speak( functions['getWeather'](command) )

			elif 'synonym' in command or 'synonyms' in command or 'similar words' in command or 'words similar to' in command:
				command = command[len(name)+1:]
				c = command.split(' ')
				wordToGetSynonymFor = c[len(c)-1]
				r = functions['getSynonyms'](wordToGetSynonymFor)
				if r == None:
					speak(f'There are no synonyms for {wordToGetSynonymFor}')
				else:
					speak( f'A synonym for {wordToGetSynonymFor} is ' + str(functions['getSynonyms'](wordToGetSynonymFor)) )

			elif 'time' in command:
				speak(f'It\'s {  datetime.now().strftime("%H %M")  }')

			else:
				print('invalid')


#