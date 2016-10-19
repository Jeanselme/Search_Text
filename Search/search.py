"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import Indexation.formatIndex as fi
import Indexation.indexation as index

def search(query, indexDirectory, reverseIndex):
	"""
	Searchs the query in the dataBase
	"""
	index.createReverseIndex(indexDirectory, reverseIndex, False)

	# Applies same changes on the query
	researchedWords = sorted(index.index(query).keys())
	possibleDocs = []
	with open(reverseIndex, 'r') as reverse:
		# Searchs the word in the reverse index
		for researchedWord in researchedWords:
			line = reverse.readline()
			word = fi.extractReverseWord(line)
			while researchedWord > word:
				line = reverse.readline()
				word = fi.extractReverseWord(line)
			# When found it, add documents to the list
			if word == researchedWord:
				# TODO : Compute the distance between documents and query
				possibleDocs += fi.extractListDocs(line)

	# TODO : Find a better way than returning the document that has the most commun
	# words (take into account, the occurence in the query)
	print("The closest doc is " + index.enumerateIndexes(indexDirectory)[int(
		max(set(possibleDocs),key=possibleDocs.count))])
