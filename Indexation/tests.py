"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""
import unittest
from indexation import *

class TestIndexation(unittest.TestCase):

	def test_extractWords(self):
		simple = "Once upon a time"
		complex = "Once upon a time, in a far!"
		ponctu = "Once upon a time , in a far !"
		assert(len(extractWords(simple)) == 4)
		assert(len(extractWords(complex)) == 7)
		assert(len(extractWords(ponctu)) == 7)

	def test_index(self):
		simple = "Once upon a time"
		complex = "Once upon a time, in a far!"
		repeat = "Once upon a time , Once upon a time!"
		assert(len(index(simple)) == 4)
		assert(len(index(complex)) == 7)
		assert(len(index(repeate)) == 4)

	def test_indexationTest(self):
		str = "Once upon a time, once upon a time"
		assert(True)

if __name__ == '__main__':
    unittest.main()
