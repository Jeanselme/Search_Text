"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import os
import sys
import Indexation.indexation as index

def help():
	print("searchEngine -indexation fileName*")
	quit()

def main():
	arg = sys.argv
	if "-indexation" in arg[1] and len(arg) > 3:
		i = 2
		fileNames = []
		while i < len(arg):
			fileNames.append(arg[i])
			i+=1
		index.indexation(fileNames, "Indexs")
	else:
		help()

if __name__ == '__main__':
	main()
