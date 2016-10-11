"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import json
import os
import urllib.request
import urllib.parse

def getSynonyms(fileName) :
	pass

def merge(dictionary) :
	"""
	Merges the dictionary respecting different synonyms
	"""
	return dictionary


# For the creation of the dictionary of synonyms
class api :
	urlDictionary = "http://www.math.sjsu.edu/~foster/dictionary.txt"

	def request(self, word):
		"""
		Creates the request adapted to the api
		"""
		word = urllib.parse.quote(word)
		return urllib.request.Request("http://watson.kmi.open.ac.uk/API/term/synonyms?term="
			+word, headers = {'Accept' : 'application/json'})

	def decode(self, response, word):
		"""
		Adapts the response to create a list of synonyms
		"""
		res = json.loads(response.read().decode('utf-8'))
		try:
			res = res["Term-array-array"]["Term-array"]["Term"]
			if isinstance(res, list):
				return res
			else:
				return [word]
		except:
			return [word]

def downloadSynonyms(word):
	"""
	Downloads the synonyms  for a given word
	"""
	watson = api()
	request = watson.request(word)
	result = []
	with urllib.request.urlopen(request) as response:
		result = watson.decode(response, word)
	return result

def downloadDictionary(dictName, url=api.urlDictionary):
	"""
	If the dictionary does not exist, it downloads all the synonyms
	"""
	if not(os.path.exists(dictName)):
		request = urllib.request.Request(api.urlDictionary)
		with urllib.request.urlopen(request) as response:
			with open(dictName, 'w') as dict:
				dict.write(response.read().decode('utf-8'))

def createDictionarySynonyms(dictName, saveName):
	"""
	Creates a file text with all the synonym of a word on each line
	Initial dictionary have to content one word by line
	"""
	downloadDictionary(dictName)
	with open(dictName, 'r') as dict:
		with open(saveName, 'w') as syno:
			for word in dict.read().split():
				syno.write(str(downloadSynonyms(word)))
