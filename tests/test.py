import unittest
import numpy as np

from dtw import dtw


class Test(unittest.TestCase):
    def test_distance(self):
        x = np.array([0, 0, 1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)
        y = np.array([1, 1, 1, 2, 2, 2, 2, 3, 2, 0]).reshape(-1, 1)
        dist, cost, acc, path = dtw(x, y, dist=lambda x, y: np.linalg.norm(x - y, ord=1))
        assert dist == 0.2

    def test_warping(self):
        x = np.array([0, 0, 1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)
        y = np.array([1, 1, 1, 2, 2, 2, 2, 3, 2, 0]).reshape(-1, 1)
        dist, cost, acc, path = dtw(x, y, dist=lambda x, y: np.linalg.norm(x - y, ord=1),
                                    warp=2)
        assert dist == 0.05

    def test_input_size(self):
        x = np.array([]).reshape(-1, 1)
        y = np.array([]).reshape(-1, 1)
        with self.assertRaises(AssertionError):
            dtw(x, y, dist=lambda x, y: np.linalg.norm(x - y, ord=1))


if __name__ == "__main__":
    unittest.main()
