#!/usr/bin/env python

# Note that indexing in python starts at 0
import numpy as np

""" Question 1"""
class NormMatrix(object):
    offset = np.array([])
    gain = np.array([])

    def __init__(self, X=[]):
        self.X = np.asarray(X, dtype=float)
        self.normalized = False
        self._calcColumnVars()

    def __getitem__(self, key):
        return self.X[key]
        
    def _calcColumnVars(self):         # This thing gets the means and stuff
        if self.X.size != 0:
            self.X = self.X.astype(float)
            self.offset = self.X.mean(axis=0)
            gain = (self.X.max(axis=0) - self.X.min(axis=0))
            self.gain = np.where(gain==0, 1, gain)

    def normalize(self):       # Offset by mean and normalize to range
        if ~self.normalized & self.X.size != 0:
            self._calcColumnVars()
            normed = (self.X - self.offset) / self.gain
            self.X = np.where(np.isnan(normed), self.X, normed)
            self.normalized = True
            
    def denormalize(self):
        if self.normalized:
            self.X = self.X*self.gain + self.offset
            normalized = False

    def addColumn(self, column):
        column = np.array(column)[np.newaxis].transpose()
        if column.size == 0:
            return
        # self.X = np.hstack((self.X, column))
        if self.X.size == 0:
            self.X = column
        else:
            self.X = np.hstack((self.X, column))
        self._calcColumnVars()
        self.normalized = False

    def addRow(self, row):
        row = np.array(row)
        if row.size == 0:
            return
        # Adding rows denormalizes the results
        if self.X.size == 0:
            self.__init__(row);
            # self.X = np.hstack((self.X, np.array(row)))
        else:
            if self.normalized:
                self.denormalize()
            self.X = np.vstack((self.X, np.array(row)))
            # self.show()    
        # self.normalize()
        self.normalized = False
        
    def show(self):
        print "------------------------------------------------"
        print "X = %s" % np.array_str(self.X, precision=2)
        print "Gain = %s" % np.array_str(self.gain, precision=2)
        print "Offset = %s" % np.array_str(self.offset, precision=2)
        print "Normalized: %s" % self.normalized
    
def q1():
    print 'Question 1'
    x = NormMatrix()
    ar = np.array([89,72,94,69])
    x.addColumn(ar)
    x.addColumn(ar**2)
    x. normalize()
    print x[1,1]
    print x[2,0]
    
def quiz():
    print '------------------------------------------------'
    q1()

if __name__ == '__main__':
    quiz()

