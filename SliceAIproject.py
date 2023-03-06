
#get a loop that collect the patent information
import numpy as np
from datetime import date
from datetime import datetime
import math
from datetime import timedelta
from dateutil.relativedelta import relativedelta, MO
from pandas import DataFrame
import pandas as pd
import os

pantents = pd.read_stata("/Users/jjw6286/Nextcloud/AI-basedEnterprises/ai_model_predictions.dta")

print(pantents.iloc[2])

pantents_any= pantents[pantents['predict50_vision']>0]

print(len(pantents_any.index))
'1517174'
print(pantents_any.iloc[2])

pantents_any['update_date'] = pd.to_datetime(pantents_any['pub_dt'])
pantents_any['year'] = pantents_any['update_date'].dt.year

print(pantents_any['year'].value_counts())

pantents_any = pantents_any[pantents_any['year']>2014]

pantents_any.to_csv("/Users/jjw6286/Nextcloud/AI-basedEnterprises/AIvisionfirm.csv",
sep=",")
