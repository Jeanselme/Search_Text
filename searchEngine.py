"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import os
import sys
import Indexation.indexation as index
import Indexation.synonymsProcessing as synonyms

def help():
	print("searchEngine -indexation fileName*")
	quit()

def main():
	arg = sys.argv
	if len(arg) < 1:
		help()
	if "-indexation" in arg[1] and len(arg) >= 3:
		fileNames = []
		for doc in arg [2:]:
			if not(os.path.exists(doc)):
				print(doc + " does not exists")
			else :
				fileNames.append(doc)
		index.indexation(fileNames, "Indexs/")
	elif "-createSynonyms" in arg[1] and len(arg) == 2:
		synonyms.createDictionarySynonyms("Dictionary/dict.txt",
			"Dictionary/synonyms.txt")
	else:
		help()

if __name__ == '__main__':
	main()
