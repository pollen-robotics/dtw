from numpy import array, zeros, argmin, inf

class DTW:

    def __init__(self):
        pass

    def fit(self, x, y, dist):
        """
        Computes Dynamic Time Warping (DTW) of two sequences.

        :param array x: N1*M array
        :param array y: N2*M array
        :param func dist: distance used as cost measure

        Returns the minimum distance, the cost matrix, the accumulated cost matrix, and the wrap path.
        """
        r, c = len(x), len(y)
        D0 = zeros((r + 1, c + 1))
        D0[0, 1:] = inf
        D0[1:, 0] = inf
        D1 = D0[1:, 1:] # view
        for i in range(r):
            for j in range(c):
                D1[i, j] = dist(x[i], y[j])
        C = D1.copy()
        for i in range(r):
            for j in range(c):
                D1[i, j] += min(D0[i, j], D0[i, j+1], D0[i+1, j])
        if len(x)==1:
            path = zeros(len(y)), range(len(y))
        elif len(y) == 1:
            path = range(len(x)), zeros(len(x))
        else:
            self.D0 = D0
            path = self._traceback(D0) # find the shortest path within cost matrix
        return D1[-1, -1] / sum(D1.shape), C, D1, path

    def _traceback(self, D):
        i, j = array(D.shape) - 2
        p, q = [i], [j]
        while ((i > 0) or (j > 0)):
            tb = argmin((D[i, j], D[i, j+1], D[i+1, j]))
            if (tb == 0):
                i -= 1
                j -= 1
            elif (tb == 1):
                i -= 1
            else: # (tb == 2):
                j -= 1
            p.insert(0, i)
            q.insert(0, j)
        return array(p), array(q)
