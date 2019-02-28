# Setting up process clock
import time
from tqdm import tqdm

# Defines the initial start time
start_time = time.time()

# Importing core packages
import pandas as pd
import numpy as np
import requests
from requests_futures.sessions import FuturesSession
from tqdm import tqdm
import matplotlib.pyplot as plt

# Adding pandas progress bar
tqdm.pandas(desc="progress")

# Importing a .csv file named 'url.csv' from the same location as this script
url_df = pd.read_csv("./url.csv")

# Defining functions to apply to url_df
def get_status_code(url):
    try:
        r = requests.get(url, timeout=10)
        return r.status_code 
    except requests.exceptions.RequestException:
        return "Exception"

# Applying functions
if __name__ == "__main__":
        url_df["status_code"] = url_df["url"].progress_apply(get_status_code)
else:
        print("Error!")

# Sending results to a file named 'siteresults.csv' in the same location as this script
url_df.to_csv("./results.csv",sep=',',index=False)

# Makes a summary_df
summary_df = url_df.groupby('status_code')['url'].count().reset_index()
print(summary_df)

# Prints difference between time at end and time at begining i.e. total process time
print("--- %f minutes ---" % ((time.time() - start_time)/60))