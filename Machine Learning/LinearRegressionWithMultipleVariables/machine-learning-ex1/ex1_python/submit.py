#!/usr/bin/env python

import numpy as np

from lib.makeValidFieldName import *
from lib.submitWithConfiguration import *

def submit():
    conf = Config()
    conf.assignmentSlug = 'linear-regression'
    conf.itemName = 'Linear Regression with Multiple Variables'
    conf.partArrays = [
        [
            '1',
            ['warmUpExcercise.m'],
            'Warm-up Excercise'
        ],
        [
            '2',
            [ 'computeCost.m' ],
            'Computing Cost (for One Variable)',
        ],
        [
            '3',
            [ 'gradientDescent.m' ],
            'Gradient Descent (for One Variable)',
        ],
        [
            '4',
            [ 'featureNormalize.m' ],
            'Feature Normalization',
        ],
        [
            '5',
            [ 'computeCostMulti.m' ],
            'Computing Cost (for Multiple Variables)',
        ],
        [
            '6',
            [ 'gradientDescentMulti.m' ],
            'Gradient Descent (for Multiple Variables)',
        ],
        [
            '7',
            [ 'normalEqn.m' ],
            'Normal Equations',
        ],
    ]
    conf.output = lambda partId: output(partId)
    output('a')

def output(partId):
    # Don't forget to transpose!!!!
    # % Random Test Cases
    X1 = np.vstack((
        np.ones((1,20)),
        np.exp(1) + np.exp(2) * np.arange(0.1,2.1,0.1)
    ))
    Y1 = (X1[1,:] + np.sin(X1[0,:]) + np.cos(X1[1,:]))
    X2 = np.vstack((X1, X1[1,:]**0.5, X1[1,:]**0.25))
    Y2 = Y1**0.5 + Y1;
    X1.transpose()
    X2.transpose()
    Y1.transpose()
    Y2.transpose()

    if partId == '1':
        out = sprintf('%0.5f ', warmUpExercise());
    elif partId == '2':
        out = sprintf('%0.5f ', computeCost(X1, Y1, [[0.5], [-0.5]]));
    elif partId == '3':
        out = sprintf('%0.5f ', gradientDescent(X1, Y1, [[0.5], [-0.5]], 0.01, 10));
    elif partId == '4':
        out = sprintf('%0.5f ', featureNormalize(X2[:,1:3]));
    elif partId == '5':
        out = sprintf('%0.5f ', computeCostMulti(X2, Y2, [[0.1], [0.2], [0.3], [0.4]]));
    elif partId == '6':
        out = sprintf('%0.5f ', gradientDescentMulti(X2, Y2, [[-0.1], [-0.2], [-0.3], [-0.4]], 0.01, 10));
    elif partId == '7':
        out = sprintf('%0.5f ', normalEqn(X2, Y2));

if __name__ == '__main__':
    submit()
