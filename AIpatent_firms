
#get the patent organizations
import requests
import numpy as np
from datetime import date
from datetime import datetime
import math
from datetime import timedelta
from dateutil.relativedelta import relativedelta, MO
from pandas import DataFrame
import pandas as pd
import os

#only get the vision AI firms

getAIfirms = pd.read_csv('/Users/jjw6286/Nextcloud/AI-basedEnterprises/AIvisionfirm.csv',sep=",")

alldata = pd.DataFrame()

#from application ID get the patent id
#match patent Id with the assignee organizations
#find public firms and subsidaries


applicationinfo = pd.read_csv('/Users/jjw6286/Downloads/g_application.tsv',sep='\t')


listAIproject = getAIfirms['appl_id'].values.astype(str).tolist()

ListAIpatent = applicationinfo1['patent_id'].values.tolist()

#dataset of basic AI patent information
#patent_id matches with appl_id

patentsdata=pd.read_csv('/Users/jjw6286/Downloads/g_patent.tsv',sep='\t')
print(patentsdata.iloc[1])

patentinfor = patentsdata[patentsdata['patent_id'].isin(ListAIpatent)]

#data set for patent assignee and assigneer organization

assigneedata=pd.read_csv('/Users/jjw6286/Downloads/g_assignee_not_disambiguated.tsv',sep='\t')
print(assigneedata.iloc[1])

#output:
#AI vision patents, patent basic infor, patent assignee and assignee organizations





