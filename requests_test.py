# Setting up process clock
import time

# Defines the initial start time
# start_time = time.time()

# Importing core packages
import pandas as pd
import numpy as np
import requests
from requests_futures.sessions import FuturesSession
from tqdm import tqdm

# Adding pandas progress bar
tqdm.pandas(desc="progress bar")

# Importing a .csv file named 'url.csv' from the same location as this script
url_df = pd.read_csv("./url.csv")

# Defining functions to apply to url_df
def get_status_code(url):
    try:
        r = requests.head(url, timeout=1)
        return r.status_code == requests.codes.ok
    except requests.exceptions.RequestException:
        return False

# Applying functions
if __name__ == "__main__":
        url_df["url_test_results"] = url_df["url"].progress_apply(get_status_code)
else:
        print("Error!")

# Sending results to a file named 'siteresults.csv' in the same location as this script
url_df.to_csv("./results.csv",sep=',',index=False)

# Prints difference between time at end and time at begining i.e. total process time
# print("--- %s seconds ---" % (time.time() - start_time))