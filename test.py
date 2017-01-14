import unittest
import numpy as np
from dtw import dtw

class dtwTest(unittest.TestCase):

	def test_distance(self):

		x = np.array([0, 0, 1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)
		y = np.array([1, 1, 1, 2, 2, 2, 2, 3, 2, 0]).reshape(-1, 1)
		dist, cost, acc, path = dtw.dtw(x, y, dist=lambda x, y: np.linalg.norm(x - y, ord=1))
		assert dist == 0.2
	
if __name__ == "__main__":
    unittest.main()