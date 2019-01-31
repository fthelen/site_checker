# Importing two packages
import pandas as pd
import numpy as np
import requests

# Importing a .csv file named 'url.csv' from the same location as this script
url_df = pd.read_csv("./url.csv")

# Converting the 'url' column series into a list to run through loop
test_list = url_df['url'].tolist()

# Generating a new list full of True/False results
results_list = []
for x in test_list:
    try:
        r = requests.get(x)
        n = r.status_code == requests.codes.ok
        results_list.append(str(n))
# This will catch all connection errors and and append them into the list    
    except requests.exceptions.RequestException as r:
         n = r == requests.codes.ok
         results_list.append(str(n))

# Adding results to new column in url_df using np.array()
url_df['url_test_result'] = pd.DataFrame(np.array(results_list))

# Sending results to a file named 'siteresults.csv' in the same location as this script
url_df.to_csv("./siteresults.csv",sep=',',index=False)