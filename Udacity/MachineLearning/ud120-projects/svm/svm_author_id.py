#!/usr/bin/env python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

from sklearn.svm import SVC
import numpy as np

features_train_sm = features_train[:len(features_train)/100] 
labels_train_sm = labels_train[:len(labels_train)/100] 

clf = SVC(kernel='rbf')
t0 = time()
clf.fit(features_train_sm, labels_train_sm)
print "Training time:", round(time()-t0, 3), "s"
t0 = time()
score = clf.score(features_test, labels_test) 
print "Testing time:", round(time()-t0, 3), "s"
print "The score is:", score

print "Optimizing C"

clfs = []
score_max = 0
for C in [10, 100, 1000, 10000]:
  clfs.append(SVC(kernel='rbf', C=C))
  clfs[-1].fit(features_train_sm, labels_train_sm)
  score = clfs[-1].score(features_test, labels_test) 
  if score > score_max:
    score_max = score
    score_C = C

clf = SVC(kernel='rbf', C = score_C)
tests = np.array([10, 26, 50])
t0 = time()
clf.fit(features_train_sm, labels_train_sm)
print "Training time:", round(time()-t0, 3), "s"
t0 = time()
score = clf.score(features_test, labels_test) 
print "Testing time:", round(time()-t0, 3), "s"
print "The score is:", score

print "Predictions:", clf.predict(features_test[tests])

# print "Max score with C = ", C, "and score of", score_max

# clf = SVC(kernel='rbf', C = score_C)
# t0 = time()
# clf.fit(features_train, labels_train)
# print "Training time:", round(time()-t0, 3), "s"
# t0 = time()
# score = clf.score(features_test, labels_test) 
# print "Testing time:", round(time()-t0, 3), "s"
# print "The score is:", score



#########################################################


