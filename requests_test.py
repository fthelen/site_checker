# Setting up process clock
import time

# Defines the initial start time
start_time = time.time()

# Importing core packages
import pandas as pd
import numpy as np
import requests

# Importing a .csv file named 'url.csv' from the same location as this script
url_df = pd.read_csv("./url.csv")

# Converting the 'url' column series into a list to run through loop
url_test_list = url_df['url'].tolist()

# Generating a new list full of True/False results
url_test_results = []
for x in url_test_list:
    try:
# The request will produce a timeout error after 5 seconds
        r = requests.get(x, timeout=5)
        n = r.status_code == requests.codes.ok
        url_test_results.append(str(n))
# This will catch all connection errors and and append them into the list    
    except requests.exceptions.RequestException as r:
         n = r == requests.codes.ok
         url_test_results.append(str(n))

# Adding results to new column in url_df using np.array()
url_df['url_test_results'] = pd.DataFrame(np.array(url_test_results))

# Sending results to a file named 'siteresults.csv' in the same location as this script
url_df.to_csv("./results.csv",sep=',',index=False)

# Prints differnece between time at end and time at begining i.e. total process time
print("--- %s seconds ---" % (time.time() - start_time))