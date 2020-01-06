import pandas as pd
import json

with open('../Data/SF_Dict.json') as f:
    SF_Dict = json.load(f)

with open('../Data/SF_Features.json') as f:
    SF_Features = json.load(f)

with open('../Data/SF_ID.json') as f:
    SF_ID = json.load(f)

print('start')

years = ['2016', '2017', '2018', '2019']
for y in years:
    file_name = f"../Data/san_francisco-censustracts-{y}-3-All-HourlyAggregate.csv"
    df = pd.read_csv(file_name, 
                     usecols=['sourceid', 
                              'dstid', 
                              'hod', 
                              'mean_travel_time', 
                              'standard_deviation_travel_time']
                     )
    result_list = []
    for start_id1 in SF_ID:
        df_rows1 = df["sourceid"] == start_id1
        for start_id2 in SF_ID:
            df_rows2 = (df[df_rows1])["dstid"] == start_id2
            df_rows2_index = df_rows2.index.to_list()
            for i in df_rows2_index:
                if df_rows2[i] == True:
                    result_list.append(i)
    SF_Sample = df.iloc[result_list, :]
    SF_Sample.to_csv(f'..\Data\SF_Sample_{y}.csv')

print('complete')

