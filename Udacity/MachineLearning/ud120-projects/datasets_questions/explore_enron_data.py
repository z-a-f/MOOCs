#!/usr/bin/env python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import re

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of people:", len(enron_data)
print "Number of features:", len(enron_data[enron_data.keys()[0]])

pois = 0
salaried = 0
emailed = 0
total_payments_nan = 0
total_payments_nan_poi = 0
for person, feats in enron_data.iteritems():
  pois += feats['poi']
  salaried += 0 if feats['salary'] == 'NaN' else 1
  emailed += 0 if feats['email_address'] == 'NaN' else 1
  total_payments_nan += 1 if feats['total_payments'] == 'NaN' else 0
  total_payments_nan_poi += 1 if feats['total_payments'] == 'NaN' and feats['poi'] else 0
print "Points of Interest:", pois
print "People with salaries:", salaried
print "People with emails:", emailed
print "People with NaN payments:", total_payments_nan * 100. / len(enron_data)
print "POIs wiht NaN payments:", total_payments_nan_poi * 100. / pois

for person, feats in enron_data.iteritems():
  if re.search(r'prentice', person.lower()):
    print person, feats, '\n'
  if re.search(r'colwell', person.lower()):
    print person, feats, '\n'
  if re.search(r'skilling', person.lower()):
    print person, feats, '\n'
  if re.search(r'lay', person.lower()):
    print person, feats, '\n'
  if re.search(r'fastow', person.lower()):
    print person, feats, '\n'
