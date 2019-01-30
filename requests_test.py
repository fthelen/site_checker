# Importing two packages
import pandas
import requests

# Importing a .csv file named 'url.csv' from the same location as this script
url_df = pandas.read_csv("./url.csv")

# Converting the 'url' column series into a list to run through loop
test_list = url_df['url'].tolist()

# Generating a new list full of True/False results
results_list = []
for x in test_list:  
    r = requests.get(x)
    n = r.status_code == requests.codes.ok
    results_list.append(str(n))

# Convert results_list into a pandas series to insert into final dataframe
results_series = pandas.Series(results_list)

# Inserting the results_series into a new dataframe column named 'resutls'
url_df.insert(loc=1,column='results',value=results_series)

# Sending results to a file named 'siteresults.csv' in the same location as this script
url_df.to_csv("./siteresults.csv",sep=',',index=False)
