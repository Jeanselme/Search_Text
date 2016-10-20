"""
	Search Engine
	by Vincent Jeanselme
	and Matthieu Clin
	vincent.jeanselme@gmail.com
"""

import sys, os
# Needs to be execute from the project source
sys.path.append(os.getcwd())

import unittest
from Indexation.indexation import *

class TestIndexation(unittest.TestCase):

	def test_index(self):
		simple = "Once upon a time"
		complex = "Once upon a time, in a far!"
		repeate = "Once upon a time , Once upon a time!"
		assert(len(index(simple)) == 3)
		assert(len(index(complex)) == 5)
		assert(len(index(repeate)) == 3)

if __name__ == '__main__':
    unittest.main()
