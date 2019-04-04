import bs4
from bs4 import BeautifulSoup
import csv
import requests
import time
import pandas as pd
import urllib
import re
import pickle

dates=[]
year=2009
for j in range(1,11):
    if j==10:
        for i in range(1,11):
            if i<10:
                dates.append(str(year)+str(0)+str(i))
            else:
                dates.append(str(year)+str(i))
    else:
        for i in range(1,13):
            if i<10:
                dates.append(str(year)+str(0)+str(i))
            else:
                dates.append(str(year)+str(i))
    year=year+1

df = pd.DataFrame()
for da in dates:

    url = "http://www.estesparkweather.net/archive_reports.php?date=" + da
    s = requests.get(url).content
    soup = BeautifulSoup(s, "html.parser")
    dict_n = {}
    table = soup.find_all('table', {'class': ''})
    for result in table[:-9]:

        tr = result.find_all("tr", {"class": ["column-light", "column-dark"]})
        for each_tr in tr:
            td = each_tr.find_all('td')
            for i in range(1):
                a = td[0].text
                b = td[1].text
                dict_n[a] = b

        temp_df = pd.DataFrame.from_dict(dict_n, orient="index").T
        df = pd.concat([df, temp_df], ignore_index=True)

df_new = df[df["Avg daily max temp"].isnull()]

df_new.drop(["Avg daily max temp","Avg daily min temp"],axis=1,inplace=True)
df_new.rename(columns={'Average temperature':'Average temperature (°F)',
'Average humidity':'Average humidity (%)',
'Average dewpoint':'Average dewpoint (°F)',
'Average barometer':'Average barometer (in)',
'Average windspeed':'Average windspeed (mph)',
'Average gustspeed':'Average gustspeed (mph)',
'Average direction':'Average direction (°deg)',
'Rainfall for month':'Rainfall for month (in)',
'Rainfall for year':'Rainfall for year (in)',
'Maximum rain per minute':'Maximum rain per minute',
'Maximum temperature':'Maximum temperature (°F)',
'Minimum temperature':'Minimum temperature (°F)',
'Maximum humidity':'Maximum humidity (%)',
'Minimum humidity':'Minimum humidity (%)',
'Maximum pressure':'Maximum pressure',
'Minimum pressure':'Minimum pressure',
'Maximum windspeed':'Maximum windspeed (mph)',
'Maximum gust speed':'Maximum gust speed (mph)',
'Maximum heat index':'Maximum heat index (°F)'},inplace=True)

df_new['Average barometer (in)'] = df_new['Average barometer (in)'].str.replace("in.","").astype('float')
df_new['Average dewpoint (°F)'] = df_new['Average dewpoint (°F)'].str.replace("°F","").astype('float')
df_new['Average humidity (%)'] = df_new['Average humidity (%)'].str.replace("%","").astype('float')
df_new['Average windspeed (mph)'] = df_new['Average windspeed (mph)'].str.replace("mph","").astype('float')
df_new['Average temperature (°F)'] = df_new['Average temperature (°F)'].str.replace("°F","").astype('float')
df_new['Average gustspeed (mph)'] = df_new['Average gustspeed (mph)'].str.replace("mph","").astype('float')
df_new['Rainfall for month (in)'] = df_new['Rainfall for month (in)'].str.replace("in.","").astype('float')
df_new['Rainfall for year (in)'] = df_new['Rainfall for year (in)'].str.replace("in.","").astype('float')

df_new.reset_index(inplace=True)
df_new.drop("index",axis=1,inplace=True)
df_test = df_new.copy()


def str_replace(df, col, val):
    list_val = []
    for ro in df[col]:
        x = ro.split(val)
        x = x[0]
        x = x.strip()
        list_val.append(x)

    # create a temp dataframe

    df_temp = pd.DataFrame(list_val, columns=[col])

    df[col] = df_temp[col]
    df[col] = pd.to_numeric(df[col], errors='raise')
    df[col] = df[col].astype('float')
    return df


str_replace(df_test,"Average direction (°deg)","°")
str_replace(df_test,"Maximum rain per minute","in")
df_test.columns

str_replace(df_test,"Maximum temperature (°F)","°")
str_replace(df_test,"Minimum temperature (°F)","°")
str_replace(df_test,"Maximum pressure","in")
str_replace(df_test,"Minimum pressure","in")
str_replace(df_test,"Maximum humidity (%)","%")
str_replace(df_test,"Minimum humidity (%)","%")
str_replace(df_test,"Maximum windspeed (mph)","mph")
str_replace(df_test,"Maximum gust speed (mph)","mph")
str_replace(df_test,"Maximum heat index (°F)","°")

list_time = []
for da in dates:

    url = "http://www.estesparkweather.net/archive_reports.php?date=" + da
    s = requests.get(url).content
    soup = BeautifulSoup(s, "html.parser")
    dict_n = {}
    table = soup.find_all('table', {'class': ''})
    for result in table[:-9]:

        tr = result.find_all("tr")

        for each_tr in tr:
            td = each_tr.find_all('td')
            break

        for i in range(1):
            a = td[0].text
            time_d = da + " " + a
            list_time.append(time_d)

df_time = pd.DataFrame(list_time)

date_new = []
for ro in df_time[0]:
    x = ro.split(" ")
    try:
        if int(x[2]) <10:
            date_new.append(x[0]+"0"+x[2])
        else:
            date_new.append(x[0]+x[2])
    except ValueError:
        continue

df_time = pd.DataFrame(date_new,columns=["Date"])
df_time["Date"] = pd.to_datetime(df_time["Date"])
df_final = pd.concat([df_time,df_test],axis=1)
df_final.set_index("Date",inplace=True)
df_final=df_final.loc[:"2018-10-28"]

with open("dataframe.pk", "wb") as file:
    pickle.dump(df_final, file)

