# The goal of this branch is to develop a method for getting one off site data required to answer the status questions
# This will later need to be itterated through to produce a large list of results from a sites dataset

import pandas
import requests

url_list = pandas.read_csv(r'C:\Users\Thele\Documents\GitHub\site_checker\sites_list.csv')

results_list = []
for row in url_list:  
    r = requests.get(row)
    n = r.status_code == requests.codes.ok
    results_list.append(str(n))
print(results_list)