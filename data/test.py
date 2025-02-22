# --coding:utf-8--
# project:
# user:User
# Author: tyy
# createtime: 2022-11-29 17:13
import pandas as pd
import os

data_list = pd.read_csv('hiddensetnames.csv')
data_list = data_list['FileName'].values

for files in os.listdir('./original_data/'):
    if files not in data_list:
        print(files)

