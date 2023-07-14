# importing speech recognition package from google api
import speech_recognition as sr
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
from Weather import *
import nltk
#nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup
import requests
from nltk.corpus import wordnet
from nltk.corpus import brown
import random


headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}


def get_audio():
	rObject = sr.Recognizer()
	audio = ''
	with sr.Microphone() as source:
		audio = rObject.listen(source, phrase_time_limit = 86400)
	try:
		command = rObject.recognize_google(audio, language ='en-US')
		return command
	except:
		return ''


def getSynonyms(word):
	word = word.replace(' ', '-')
	search = requests.get(f'https://www.dictionary.com/browse/{word}', headers = headers)
	soup = BeautifulSoup(search.text, 'html.parser')
	try:

		synonyms = soup.find('div', {'e15p0a5t1'}).get_text().split(', ')
		if len(synonyms) == 0:
			return None

		print(synonyms)
		r = random.choice(synonyms)
		return r
	except:
		print('invalid')


if __name__ == '__main__':
	while True:
		getSynonyms(get_audio())
























#