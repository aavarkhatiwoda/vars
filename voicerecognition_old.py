# importing speech recognition package from google api
import speech_recognition as sr
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
from weather import *
import pyttsx3 as tts

functions = {'getWeather':getWeather}



num = 1
def speak(output):
	global num

	# num to rename every audio file
	# with different name to remove ambiguity
	num += 1
	#print("Person : ", output)

	print(output)
	toSpeak = gTTS(text = output, lang='en')
	# saving the audio file given by google text to speech
	file = str(num) + ".mp3"
	toSpeak.save(file)

	# playsound package is used to play the same file.
	playsound.playsound(file, True)
	#os.remove(file)



def get_audio():

	rObject = sr.Recognizer()
	audio = ''

	with sr.Microphone() as source:
		#print("Speak...")

		# recording the audio using speech recognition
		audio = rObject.listen(source, phrase_time_limit = 86400)
	#print("Stop.") # limit 5 secs

	try:

		command = rObject.recognize_google(audio, language ='en-US')
		#print("You : ", text)
		print(command)
		return command

	except:

		#speak("Could not understand your audio, PLease try again !")
		#return 0
		return ''




# Driver Code
if __name__ == "__main__":

	rava ='rava'

	'''
	def defineSpeaker():
		speaker = tts.init()
		speaker.setProperty('rate', 150)
	'''

	while True:

		command = get_audio().lower()

		if 'wrap it up' in command or 'close up shop' in command:
			speak('See you tomorrow, sir.')
			exit(0)

		elif 'you there' in command:
			#speak('At your service, sir.')
			tts.init().say('At your service, sir')

		elif 'my name' in command:
				speak('Sir, please don\'t assume I am that low of an assistant to not know your name.')

		elif 'weather' in command or 'temperature' in command or 'forecast' in command:
			#speak(getWeather(text))
			speak( functions['getWeather'](command) )

		elif 'open' in command:
			if '.'in command:
				command = command[command.index('open ') + 5:].replace(' ', '')
				os.system(f'open http://www.{command}')
			else:
				command = command[command.index('open ') + 5:].replace(' ', '')
				os.system(f'open http://www.{command}' + '.com')

		else:
			print('invalid')
			#speak('I\'m afraid that command hasn\'t been implemented yet, try again or \'close shop\'.')





'''
	while True:
		text = get_audio().lower()
		if text == 'dummy':
			speak("What can I do for you, sir?")
			text = get_audio().lower()
			text = str(text)

			if 'pack it up' in text:
				speak('See you tomorrow, sir.')
				exit(0)

			elif 'weather' or 'temperature' or 'forecast' in text:
				assistnt_speaks(getWeather(text))

			else:
				speak('I\'m afraid that command hasn\'t been implemented yet, try again, sir\'.')
	'''










"""
	while(1):

		#speak("What can i do for you?")
		text = get_audio().lower()

		if text == 'dummy':
			speak('At your command, sir.')

			text = get_audio().lower()

			if 'close shop' in str(text):
				speak('See you tomorrow, sir.')
				break

			elif 'weather' in text:
				speak(getWeather(text))

			else:
				speak('I\'m afraid that command hasn\'t been implemented yet, try again or \'close shop\'.')
			continue
"""





























#
