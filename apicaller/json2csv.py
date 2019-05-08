import sys
import pandas as pd
from pandas import DataFrame
import json

from pandas.io.json import json_normalize 


data=r"apicaller/darsky_asuncion_response_raw.json"
# print ("This is json data input", data)

# Reads and converts json to dict.
def js_r(data):
   with open(data, encoding='utf-8') as f_in:
       return(json.load(f_in))

my_dic_data = js_r(data)
result = json_normalize(my_dic_data)

print(result['daily.data'])

print(result.iloc[0])
