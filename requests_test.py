# Importing two packages
import pandas
import requests

# Importing a .csv file named 'url.csv' from the same location as this script
url_df = pandas.read_csv("./url.csv")

# Converting the 'url' column series into a list to run through loop
test_list = url_df['url'].tolist()

# Generating a new list full of True/False results from 
results_list = []
for x in test_list:  
    r = requests.get(x)
    n = r.status_code == requests.codes.ok
    results_list.append(str(n))

# Converting the results list into a pandas dataframe to use the .to_csv to generate a usable file
export_df = pandas.DataFrame(data=results_list)

# Sending results to a file named 'siteresults.csv' in the same location as this script
export_df.to_csv("./siteresults.csv",sep=',',index=False)