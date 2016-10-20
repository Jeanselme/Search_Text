"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import sys, os
# Needs to be execute from the project source
sys.path.append(os.getcwd())

from Indexation.formatIndex import *
import unittest

class TestFormatIndex(unittest.TestCase):
	"""
	Tests if the different functions are bijections
	"""

	def test_extractWord(self):
		text = writeIndex("word", 17)
		assert(extractWord(text) == "word")

	def test_extractOccurence(self):
		text = writeIndex("word", 17)
		assert(extractOccurence(text) == "17")


	def test_extractReverseWord(self):
		reverseIndex = writeReverseIndex("word", [1,2], [5,6])
		assert(extractReverseWord(reverseIndex) == "word")

	def test_extractListDocs(self):
		reverseIndex = writeReverseIndex("word", [1,2], [5,6])
		assert(extractListDocs(reverseIndex) == [1,2])

if __name__ == '__main__':
    unittest.main()
