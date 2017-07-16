#!/usr/bin/env python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


# #### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
# ################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import numpy as np

from tqdm import tqdm

print np.shape(features_train)

# dt = DecisionTreeClassifier()
svm = SVC(kernel='linear')
# clf = AdaBoostClassifier(n_estimators=50, base_estimator=dt,learning_rate=1)
# clf = AdaBoostClassifier(algorithm='SAMME.R', base_estimator=dt)
clf = AdaBoostClassifier(algorithm='SAMME', base_estimator=svm)
clf.fit(features_train, labels_train)
max_score = clf.score(features_test, labels_test)
params = None
# for split_num in tqdm(range(2, 6)):
#   for depth in tqdm(range(1, 10)):
# for estimators in tqdm(xrange(2, 50, 2)):
#   for learn_rate in tqdm(np.arange(1, 10, 0.5), postfix={'Score':max_score, 'Params': params}):
#     clf.set_params(n_estimators=estimators, learning_rate=learn_rate)
#     clf.fit(features_train, labels_train)
#     score = clf.score(features_test, labels_test)
#     if score >= max_score:
#       max_score = score
#       params = (estimators, learn_rate)

print max_score, params
# Found: 20, 2.0

# max_score = 0
# params = None
# list_estimators = [19, 20, 21]
# list_learn_rate = np.arange(1.5, 2.5, 0.1)
# for estimators in tqdm(list_estimators):
#   for learn_rate in tqdm(list_learn_rate, postfix={'Score':max_score}):
#     clf.set_params(n_estimators=estimators, learning_rate=learn_rate)
#     clf.fit(features_train, labels_train)
#     score = clf.score(features_test, labels_test)
#     if score >= max_score:
#       max_score = score
#       params = (estimators, learn_rate)
# print
# print max_score, params


try:
    prettyPicture(clf, features_test, labels_test)
except NameError as e:
    print "NameError", e
except:
    print "Could not show picture"
