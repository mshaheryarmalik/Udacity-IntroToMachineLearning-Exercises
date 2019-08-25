#!/usr/bin/python

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
from sklearn.metrics import accuracy_score
from sklearn import svm

clf = svm.SVC(kernel='rbf', C=10000)
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
start = time()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print "training time:", round(time()-start, 3), "s"
print(accuracy_score(labels_test, pred))

# sara = 0
# chris = 0
# i = 0
# while i < 1758:
#     if pred[i] is 0:
#         sara = sara + 1
#     elif pred[i] is 1:
#         chris = chris + 1
#     i = i + 1
#
# print sara, chris
count = 0
for i in pred:
    print i
    if i is 1:
        count = count + 1

print count
#########################################################


