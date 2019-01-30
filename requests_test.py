# The goal of this branch is to develop a method for getting one off site data required to answer the status questions
# This will later need to be itterated through to produce a large list of results from a sites dataset

import pandas
import requests

url_df = pandas.read_csv("./url.csv")

test_list = url_df['url'].tolist()

results_list = []
for x in test_list:  
    r = requests.get(x)
    n = r.status_code == requests.codes.ok
    results_list.append(str(n))

export_df = pandas.DataFrame(data=results_list)
export_df.to_csv("./siteresults.csv",sep=',',index=False)