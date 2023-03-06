
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
'''doc_id                 20040254117
flag_patent                      0
pub_dt                  2004-12-16
appl_id                   09908955
flag_train_any                   0
predict50_any_ai                 0
flag_train_ml                    0
ai_score_ml               0.000881
predict50_ml                     0
flag_train_evo                   0
ai_score_evo              0.002197
predict50_evo                    0
flag_train_nlp                   0
ai_score_nlp              0.001464
predict50_nlp                    0
flag_train_speech                0
ai_score_speech           0.004977
predict50_speech                 0
flag_train_vision                0
ai_score_vision           0.000985
predict50_vision                 0
flag_train_kr                    0
ai_score_kr               0.000365
predict50_kr                     0
flag_train_planning              0
ai_score_planning          0.00042
predict50_planning               0
flag_train_hardware              0
ai_score_hardware         0.001134
predict50_hardware               0
analysis_phase                   1
Name: 2, dtype: object'''


pantents_any= pantents[pantents['predict50_vision']>0]

print(len(pantents_any.index))
'''1517174'''

print(pantents_any.iloc[2])

pantents_any['update_date'] = pd.to_datetime(pantents_any['pub_dt'])
pantents_any['year'] = pantents_any['update_date'].dt.year

print(pantents_any['year'].value_counts())

pantents_any = pantents_any[pantents_any['year']>2014]

#appl_id is used to match with other patent information

pantents_any.to_csv("/Users/jjw6286/Nextcloud/AI-basedEnterprises/AIvisionfirm.csv",
sep=",")
