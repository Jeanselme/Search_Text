"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import os
import sys
import Search.search as search
import Indexation.indexation as index
import Indexation.synonymsProcessing as synonyms

def help():
	print("searchEngine (-indexation fileName* |-createSynonyms |-search \"Expression\")")
	quit()

def main():
	arg = sys.argv
	if len(arg) < 2:
		help()
	if "-indexation" in arg[1] and len(arg) >= 3:
		fileNames = []
		for doc in arg [2:]:
			if not(os.path.exists(doc)):
				print(doc + " does not exists")
			else :
				fileNames.append(doc)
		index.indexation(fileNames, "Indexs/", "Indexs/newReverseIndex.rev")
	elif "-createSynonyms" in arg[1] and len(arg) == 2:
		synonyms.createDictionarySynonyms("Dictionary/dict.txt",
			"Dictionary/synonyms.txt")
	elif "-search" in arg[1] and len(arg) == 3:
		search.search(arg[2], "Indexs/", "Indexs/newReverseIndex.rev")
	else:
		help()

if __name__ == '__main__':
	main()
