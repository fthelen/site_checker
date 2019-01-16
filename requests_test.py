# The goal of this branch is to develop a method for getting one off site data required to answer the status questions
# This will later need to be itterated through to produce a large list of results from a sites dataset

import requests

r = requests.get('http://www.google.com')
print(r.text)

url_list = ['http://www.google.com','http://www.netflix.com']

r_list = requests.get(url_list)
print(url_list.text)