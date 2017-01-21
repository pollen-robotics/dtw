# dtw

## what is this?

dtw (dynamic time warping) python module. it is effectively a distance metric - small distance values indicate similarity.

## where do i get it?

from pypi:
```
python -m pip install dtw
```

from source:
```
git clone https://github.com/mynameisvinn/dynamic-time-warping
cd dynamic-time-warping
python setup.py install
```

## how do i use it?
```
>>> from dtw import DTW
>>> x = np.array([0, 0, 1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)
>>> y = np.array([1, 1, 1, 2, 2, 2, 2, 3, 2, 0]).reshape(-1, 1)
>>> D = DTW()
>>> dist, cost, acc, path = D.fit(x, y, dist=lambda x, y: np.linalg.norm(x - y, ord=1))
```

## how does it work?
dtw calculates pairwise distances (eg manhattan, euclidean) for two series of points. then, the shortest path between start and end points, in terms of cumulative distance, is identified.


## examples

examples are available as notebook:

* [a simple example](http://nbviewer.ipython.org/github/pierre-rouanet/dtw/blob/master/simple%20example.ipynb)
* [a sound comparison based on DTW + MFCC](http://nbviewer.ipython.org/github/pierre-rouanet/dtw/blob/master/MFCC%20%2B%20DTW.ipynb)
* [simple speech recognition](http://nbviewer.ipython.org/github/pierre-rouanet/dtw/blob/master/speech-recognition.ipynb)
