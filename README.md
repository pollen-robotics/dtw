# dtw

## what is this?

dtw (dynamic time warping) python module. it is effectively a distance metric - small distance values indicate similarity.

## install

```
python -m pip install dtw
```

## how does it work?
dtw calculates pairwise distances (eg manhattan, euclidean) for two series of points. then, the "shortest" path, as defined by cumulative distance, between start and end points is identified.


## examples

examples are available as notebook:

* [a simple example](http://nbviewer.ipython.org/github/pierre-rouanet/dtw/blob/master/simple%20example.ipynb)
* [a sound comparison based on DTW + MFCC](http://nbviewer.ipython.org/github/pierre-rouanet/dtw/blob/master/MFCC%20%2B%20DTW.ipynb)
* [simple speech recognition](http://nbviewer.ipython.org/github/pierre-rouanet/dtw/blob/master/speech-recognition.ipynb)
