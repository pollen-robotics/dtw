import unittest
import numpy as np

from dtw import dtw, accelerated_dtw


class FastVsNormalTestCase(unittest.TestCase):
    def test_fast_vs_normal_1D(self):
        x = np.random.rand(np.random.randint(2, 100))
        y = np.random.rand(np.random.randint(2, 100))

        d1, c1, acc1, p1 = dtw(x, y, dist=lambda x, y: np.abs((x - y)))
        d2, c2, acc2, p2 = accelerated_dtw(x, y, 'euclidean')

        self.assertAlmostEqual(d1, d2)
        self.assertAlmostEqual((c1 - c2).sum(), 0)
        self.assertAlmostEqual((acc1 - acc2).sum(), 0)
        self.assertTrue((p1[0] == p2[0]).all())
        self.assertTrue((p1[1] == p2[1]).all())

    def test_fast_vs_normal_ND(self):
        N = np.random.randint(2, 100)
        m1 = np.random.randint(2, 100)
        m2 = np.random.randint(2, 100)

        x = np.random.rand(m1, N)
        y = np.random.rand(m2, N)

        d1, c1, acc1, p1 = dtw(x, y, dist=lambda x, y: np.linalg.norm((x - y)))
        d2, c2, acc2, p2 = accelerated_dtw(x, y, 'euclidean')

        self.assertAlmostEqual(d1, d2)
        self.assertAlmostEqual((c1 - c2).sum(), 0)
        self.assertAlmostEqual((acc1 - acc2).sum(), 0)
        self.assertTrue((p1[0] == p2[0]).all())
        self.assertTrue((p1[1] == p2[1]).all())

    def test_specific_case(self):
        x = np.array([1.0, 0.9, 1.2, 2.3, 3.8, 3.3, 4.2, 1.9, 0.5, 0.3, 0.3])
        y = np.array([0.5, 1.0, 0.9, 1.2, 2.3, 3.8, 3.3, 4.2, 1.9, 0.5, 0.3])

        euclidean = lambda x, y: np.abs((x - y))

        d1, _, _, _ = accelerated_dtw(x, y, 'euclidean')
        d2, _, _, _ = accelerated_dtw(x, y, dist=euclidean)
        d3, _, _, _ = dtw(x, y, dist=euclidean)

        self.assertAlmostEqual(d1, 0.5)
        self.assertAlmostEqual(d2, 0.5)
        self.assertAlmostEqual(d3, 0.5)
