"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

from nltk.stem.lancaster import LancasterStemmer

def extractWords(text):
	"""
	Extracts words of a text and suppress ponctuation
	"""
	res = []
	for word in text.split() :
		newWord = ""
		for letter in word.lower() :
			# Adds only letter
			if letter in "abcdefghijklmnopqrstuvwxyz" :
				newWord += letter
			# If there is a special character, adds the word and creates a new one
			elif newWord != "":
				res.append(newWord)
				newWord = ""
		if newWord != "":
			res.append(newWord)
	return res

def stemming(words):
	"""
	Stems words and delete meaningless words
	"""
	st = LancasterStemmer()
	result = []
	meaninglessWords = ["a", "an", "i", "its", "her", "him", "me", "our", "that",
		"the", "there", "these", "them", "they", "this", "we", "you", "your"]
	for word in words:
		# Deletes meanindless words
		if not(word in meaninglessWords):
			result.append(st.stem(word))
	return result
