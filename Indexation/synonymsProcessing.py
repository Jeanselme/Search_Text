"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import json
import os
import pickle
import urllib.request
import urllib.parse
from nltk.stem.lancaster import LancasterStemmer

saveDictionarySynonyms = "Indexs/Synonyms.save"

def getDictSynonyms(saveName):
	"""
	Returns the dictionary of synonyms
	"""
	return pickle.load(open(saveDictionarySynonyms, 'rb'))

def merge(stems, saveName = saveDictionarySynonyms):
	"""
	Changes the different stems by their synonyms
	"""
	synonyms = getDictSynonyms(saveName)
	res = []
	for stem in stems:
		res.append(synonyms[stem])
	return res

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

def createDictionarySynonyms(dictName, saveNameSynonyms, saveNameCompressed = saveDictionarySynonyms):
	"""
	Creates a file text with all the synonym of a word on each line
	Initial dictionary have to content one word by line
	"""
	if not(os.path.exists(saveNameCompressed)):
		downloadDictionary(dictName)
		st = LancasterStemmer()
		res = {}
		with open(dictName, 'r') as dict:
			with open(saveNameSynonyms, 'w') as syno:
				words = dict.read().split()
				i = 0
				for word in words[:1000]:
					print(str(i) + ' / ' + str(len(words)), end="\r")
					synonyms = downloadSynonyms(word)
					syno.write(str(synonyms))
					res[st.stem(word)] = st.stem(synonyms[0])
					i += 1
		print(str(res))
		pickle.dump(res, open(saveNameCompressed, 'wb'))
	else:
		print("Dictionary seems to already exist")
