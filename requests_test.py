# The goal of this branch is to develop a method for getting one off site data required to answer the status questions
# This will later need to be itterated through to produce a large list of results from a sites dataset

import pandas
import requests

url_list = pandas.read_csv(r'C:\Users\Thele\Documents\GitHub\site_checker\url.csv')
print(url_list)

test_list = url_list("url").tolist()

results_list = []
for x in test_list:  
    r = requests.get(x)
    n = r.status_code == requests.codes.ok
    results_list.append(str(n))

print(results_list)