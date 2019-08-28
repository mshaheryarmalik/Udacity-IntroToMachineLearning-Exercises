#!/usr/bin/python

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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print "Total People", len(enron_data)

poi_count = 0
for person_name, featues in enron_data.iteritems():
    print person_name, featues
    if featues["poi"] is True:
        poi_count = poi_count + 1
print "POI Count: ", poi_count

print "Stock belonging to James Prentice: ", enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Emails count from Wesley Colwell to poi: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "The value of stock options exercised by Jeffrey K Skilling: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print len( [ enron_data[person]['total_payments'] for person in enron_data if (enron_data[person]['total_payments'] =='NaN') ])
