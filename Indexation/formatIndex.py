"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

"""
	This library contains all functions which are related to the indexes format
"""

# Format index
## Read
def extractWord(text):
	"""
	Extracts the word on the first position
	"""
	return text.rstrip('\n').split(':')[0]

def extractOccurence(text):
	"""
	Extracts the occurence of the word
	"""
	return text.rstrip('\n').split(':')[1]

## Write
def writeIndex(word, occurence):
	"""
	Writes the index
	word:occurence\n
	"""
	return word + ':' + str(occurence) + '\n'

# Format reverse index
## Read
def extractReverseWord(text):
	"""
	Extracts the word on the first position
	"""
	return text.rstrip('\n').split(':')[0]

def extractListDocs(text):
	"""
	Extracts the list of docs which contains the word
	"""
	docs = text.rstrip('\n').split(':')[1][:-1]
	docs = docs.split(';')
	res = []
	for doc in docs:
		res.append(doc[1:doc.index(',')])
	return res

## Write
def writeReverseIndex(word, documentsList, occurencesList):
	"""
	Write the reverse index
	word:(docId,Occurences);*\n
	"""
	res = word + ':'
	for i in range(len(documentsList)):
		res += '({},{});'.format(documentsList[i], occurencesList[i])
	return res + '\n'
