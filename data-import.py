import requests
import pandas as pd
import pickle

from config import *
from datetime import datetime

# Get data from FCA website
data_request = requests.get(data_url).content

# Convert to Pandas object
raw_shorts = pd.ExcelFile(data_request)
# Get sheet names, and then find sheets with the predefined substrings as an attempt to mitigate mis-selecting sheets
raw_shorts_sheetnames = raw_shorts.sheet_names

''' Predefined sheet names - change this as the FCA does '''
curr_disc_name = "Current Disclosures"
hist_disc_name = "Historic Disclosures"

# Grab sheets with predefined substrings
curr_sheet_list = list(s for s in raw_shorts_sheetnames if curr_disc_name in s)
hist_sheet_list = list(s for s in raw_shorts_sheetnames if hist_disc_name in s)

if len(curr_sheet_list) != 1 or len(hist_sheet_list) != 1:
    exit("ERROR : Check Underlying File, Sheet Names Unexpected")

curr_disclosures = pd.read_excel(data_request, sheet_name=curr_sheet_list)
hist_disclosures = pd.read_excel(data_request, sheet_name=hist_sheet_list)

# Save down dict of dataframes for historical comparison
disclosures_dict = {'current': curr_disclosures, 'historic': hist_disclosures}

# Get date from sheet name to prevent incorrectly marking data and to deal with weekends/holidays
relevant_date = curr_sheet_list[0].replace(curr_disc_name, '')
relevant_date_clean = relevant_date.replace(' ', '')
print(relevant_date_clean)


with open(data_dir + '/disclosures ' + str(relevant_date_clean) + '.pickle', 'wb') as handle:
    pickle.dump(disclosures_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)