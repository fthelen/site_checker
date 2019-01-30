# The goal of this branch is to develop a method for getting one off site data required to answer the status questions
# This will later need to be itterated through to produce a large list of results from a sites dataset

import requests
url_list = ['http://google.com', 'http://amazon.com', 'http://fanfiction.net']

results_list = []
for x in url_list:  
    r = requests.get(x)
    n = r.status_code == requests.codes.ok
    results_list.append(str(n))
print(results_list)