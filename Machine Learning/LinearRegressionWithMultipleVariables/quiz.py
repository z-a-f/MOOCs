#!/usr/bin/env python

# Note that indexing in python starts at 0
import numpy as np

""" Question 1"""
class NormMatrix(object):
    """
    mean = np.array([])
    minimum = np.array([])
    maximum = np.array([])
    """
    offset = np.array([])
    gain = np.array([])

    def __init__(self, X=[]):
        self.X = np.asarray(X, dtype=float)
        self.normalized = False
        self._calcColumnVars()

    def __getitem__(self, key):
        return self.X[key]
        
    def _calcColumnVars(self):         # This thing gets the means and stuff
        if self.X.shape != (0,):
            self.X = self.X.astype(float)
            self.offset = self.X.mean(axis=0)
            gain = (self.X.max(axis=0) - self.X.min(axis=0))
            self.gain = np.where(gain==0, 1, gain)

            """
            self.mean = self.X.mean(axis=0)
            self.minimum = self.X.min(axis=0)
            self.maximum = self.X.max(axis=0)
            """

    def normalize(self):       # Offset by mean and normalize to range
        if ~self.normalized:
            # normed = (self.X - self.mean) / (self.maximum - self.minimum)
            normed = (self.X - self.offset) / self.gain
            self.X = np.where(np.isnan(normed), self.X, normed)
            self.normalized = True

    def addColumn(self, column):
        self.X = hstack(self.X, column)
        self.normalized = False
        
    def show(self):
        print "X = %s"%np.array_str(self.X, precision=2)
        print "Mean = %s"%np.array_str(self.mean, precision=2)
        print "Min = %s"%np.array_str(self.minimum, precision=2)
        print "Max = %s"%np.array_str(self.maximum, precision=2)
        print "Normalized: %s"%self.normalized
    
def q1():
    print 'Question 1'
    x = NormMatrix([1])
    x.show()
    # x.addColumn(
    """
    x = np.array([
        [89,72,94,69]]
    )
    x = np.append(x, x**2, axis=0)
    x = x.transpose()

    y = np.array([96, 44, 87, 78])

    x,_ = normalize(x)
    # print x
    _.cout()
    """

def quiz():
    print '------------------------------------------------'
    q1()

if __name__ == '__main__':
    quiz()
    """
    X = NormMatrix(np.array([[1,1,1,1], [89,72,94,69], [1,2,3,4]]).transpose())
    X.show()
    X.normalize()
    X.show()
    """
