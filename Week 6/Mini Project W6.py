"""
RECORD CHECK  -  my version
===========================

Name  : Mohammad Haidar Ali Tajoo
Lane  :   / Cyber /       (delete two)
Date  :  31.10.2026


"""

import pandas as pd
df = pd.read_csv("cybersecurity_sample.csv")


df["Percent"] = (df["FAILED_LOGINS"] / df["TOTAL_ATTEMPTS"]) * 100 #adding a percent column to the csv file


df["Status"] = df["Percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK"))
"""adding a status column that will display: status = OVER LIMIT if percent >= 100 else WARNING if percent >= 90 else OK"""
#lambda p:, where p is taking df["Percent"] as an argument



#create a filter that will filter the not OK results
not_ok_filter = df["Status"] != "OK" 
not_ok = df[not_ok_filter]


print("=" * 64)
print("IP LOGS:")
print("=" * 64)
print(df)
print("=" * 64)
print("UNUSUAL ACTIVITY:")
print("=" * 64)
print(not_ok)
print("=" * 64)


