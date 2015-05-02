#!/usr/bin/env python

# Note that indexing in python starts at 0
import numpy as np

""" Question 1"""
class Norm(object):
    def __init__(self, mean=[], minimum=[], maximum=[]):
        self.mean = mean
        self.minimum = minimum
        self.maximum = maximum
    def cout(self):
        print "Mean:\t%s"%np.array_str(self.mean)
        print "Min:\t%s"%np.array_str(self.minimum)
        print "Max:\t%s"%np.array_str(self.maximum)
    def add(self, mean, minimum, maximum):
        self.mean = np.append(self.mean, mean)
        self.minimum = np.append(self.minimum, minimum)
        self.maximum = np.append(self.maximum, maximum)
        
def normalize(a):
    a = a.transpose()           # columns are now rows
    norm = Norm()
    for ii in range(0, len(a)):
        norm.add(np.mean(a[ii]), np.min(a[ii]), np.max(a[ii]))
        row = (a[ii] - norm.mean[ii]) / np.abs(norm.maximum[ii] - norm.minimum[ii])
        print row
        a[ii,:] = np.array(row)
        print a
    return (a, norm)
    


def q1():
    print 'Question 1'
    x = np.array([
        [89,72,94,69]]
    )
    x = np.append(x, x**2, axis=0)
    x = x.transpose()

    y = np.array([96, 44, 87, 78])

    x,_ = normalize(x)
    # print x
    _.cout()

def quiz():
    print '------------------------------------------------'
    q1()

if __name__ == '__main__':
    quiz()
