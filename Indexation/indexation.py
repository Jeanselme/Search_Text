"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import os
import sys
import Indexation.formatIndex as fi
import Indexation.wordProcessing as wp
import Indexation.synonymsProcessing as sp

def indexation(nameFiles, indexDirectory, reverseIndex):
	"""
	Indexes all the given files, contained in nameFiles, in the indexDirectory
	"""
	for name in nameFiles:
		with open(name) as file:
			dict = index(file.read())
			save(dict, indexDirectory + name + ".index")
			print("Indexation of : " + name + " done")
	createReverseIndex(indexDirectory, reverseIndex, True)
	print("Reverse index created !")

def enumerateIndexes(indexDirectory):
	"""
	Enumerates all the ".index" documents in the given directory
	"""
	filesToOpen = []
	for index in os.listdir(indexDirectory):
		if ".index" in index:
			filesToOpen.append(indexDirectory + index)
		elif os.path.isdir(index):
			filesToOpen += enumerateIndexes(indexDirectory + index + '/')
	return filesToOpen

def endReadFiles(wordsList):
	"""
	Return true if all words in the list are empty
	"""
	for word in wordsList:
		if word != '':
			return False
	return True

def selectWord(words):
	"""
	Selects the good word in the list and return the different information
	(word, (documentId, occurences)*)
	"""
	resWord = ''
	resDocuments = []
	resOccurences = []
	for i in range(len(words)):
		# There is a word which is not null due to while condition
		if words[i] != '':
			word = fi.extractWord(words[i])
			occurence = fi.extractOccurence(words[i])
			if resWord == '' or resWord > word :
				resWord = word
				resDocuments = [i]
				resOccurences = [occurence]
			# Same words => Adds the documentId
			elif resWord == word:
				resDocuments.append(i)
				resOccurences.append(occurence)

	return resWord, resDocuments, resOccurences

def createReverseIndex(indexDirectory, reverseIndex, force):
	"""
	Creates the reverse table in order to have a fester research through the document,
	instead of looking for doc which content some specific words,
	we look for specific word and see the associated documents.
	word:(docId,occurences)* -> docId is dependent of the number of document !
	"""
	if force and os.path.exists(reverseIndex):
		os.rename(reverseIndex, indexDirectory + "oldReverseIndex.backup")
	if not(os.path.exists(reverseIndex)):
		pointersFile = []
		# To do not use all the memory we compute the reverse index by comparing
		# the pointer on each document
		indexes = enumerateIndexes(indexDirectory)
		if len(indexes) == 0:
			print("No index found in the given path")
			quit()

		# Opens the different files
		for index in indexes:
			pointersFile.append(open(index, "r"))

		with open(reverseIndex, "w") as reverse:
			words = [file.readline() for file in pointersFile]
			while not(endReadFiles(words)):
				word, documents, occurences = selectWord(words)
				reverse.write(fi.writeReverseIndex(word, documents, occurences))
				for doc in documents:
					# Read a new line of the different documents
					# from which we take a word
					words[doc]= pointersFile[doc].readline()

		# Closes the different files
		for pointer in pointersFile:
			pointer.close()

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
	#res = sp.merge(res)
	return res

def save(dictionary, name):
	"""
	Saves the dictionary at the given name
	"""
	with open(name, 'w') as dest:
		for word, number in sorted(dictionary.items()):
			dest.write(fi.writeIndex(word, number))
