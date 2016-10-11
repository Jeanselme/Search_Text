"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import sys
import json
import Indexation.wordProcessing as wp
import Indexation.synonymsProcessing as sp

def indexation(nameFiles, indexDirectory):
	"""
	Indexes all the given files, contained in nameFiles, in the indexDirectory
	"""
	for name in nameFiles:
		with open(name) as file:
			dict = index(file.read())
			save(dict, indexDirectory + name + ".index")

def index(text):
	"""
	Computes the index of the given text and return it as a dictionary of words
	and frequency
	"""
	words = wp.extractWords(text)
	words = wp.stemming(words)
	res = {}
	for word in words:
		try:
			res[word] += 1
		except Exception as e:
			res[word] = 1
	res = sp.merge(res)
	return res

def save(dictionary, name):
	with open(name, 'w') as dest:
		dest.write(json.dumps(dictionary,sort_keys=True,indent=4, separators=(',', ': ')))
