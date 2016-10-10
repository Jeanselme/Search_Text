"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import sys
import hashlib

def hashIndexWords(word):
	"""
	Computes the hash of the given word
	"""
	return hashlib.md5(word.encode())

def extractWords(text):
	"""
	Extracts words of a text and suppress ponctuation
	"""
	res = []
	for word in text.split() :
		newWord = ""
		for letter in word.lower() :
			if letter in "abcdefghijklmnopqrstuvwxyz" :
				newWord += letter
		if newWord != "":
			res.append(newWord)
	return res

def stemming(words):
	"""
	Stems words and delete meaningless words
	"""
	# TODO : Find a library which computes it
	return words

def indexation(nameFiles, indexDirectory):
	"""
	Indexes all the given files, contained in nameFiles, in the indexDirectory
	"""
	for name in nameFiles:
		if not(os.path.exists(modelFileName)):
			print(name + " does not exists")
		else :
			with open(name) as file:
				dict = index(file.read())
				save(dict, name + ".index")

def index(text):
	"""
	Computes the index of the given text and return it as a dictionnary of words
	and frequency
	"""
	words = extractWords(text)
	words = stemming(words)
	res = {}
	for word in words:
		hashWord = hashIndexWords(word)
		try:
			res[hashWord] += 1
		except Exception as e:
			res[hashWord] = 1
	return res

def save(dictionnary, name):
	with open(name, 'w') as dest:
		dest.write(dictionnary)
