#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print accuracy_score(labels_test, pred)

print "POIs for test set", sum(pred)
print "Total people in test set", len(pred)
print "New Accuracy: ", pred.tolist().count(0) / float(len(pred))
true_positives = 0
for i in range(len(pred)):
    if (pred[i] == labels_test[i]) and labels_test[i] == 1:
        true_positives += 1
print "True Positives: ", true_positives
print "Precision score:", precision_score(pred, labels_test)
print "Recall score:", recall_score(pred, labels_test)