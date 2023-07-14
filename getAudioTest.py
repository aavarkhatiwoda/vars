# importing speech recognition package from google api
import speech_recognition as sr
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
#from weather import *
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
#nltk.download("stopwords")
from nltk.corpus import stopwords

#stop_words = set(stopwords.words("english"))
#filtered_list = []

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
		#return command
		command.replace('.', '')
		command.replace(',', '')
		c = command.split(' ')
		print(c)
		for i in c:
				print(i)
		print()

	except:

		#speak("Could not understand your audio, PLease try again !")
		#return 0
		return ''


if __name__ == "__main__":

	name ='The Dark Lord'

	while True:

		get_audio()