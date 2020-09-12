import requests as rq
import sqlite3

r = rq.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-0AD45098-4367-4EDC-8CA6-A1AFA43558EC")
#print(r.status_code)

l = r.json()
#print(type(l))

#確認資料的長相...?
"""
print("l的 key 有",l.keys())
print("l['records']的 key 有",l['records'].keys(),"型態: ",type(l['records']))
print("l['records']['location']的型態: ",type(l['records']['location']))
print("(l['records']['location'])[0]的型態",type((l['records']['location'])[0]),"key有 ",l['records']['location'][0].keys())
print("(l['records']['location'])[0]['weatherElement']的型態",type((l['records']['location'])[0]['weatherElement']))
print(len((l['records']['location'])[0]['weatherElement']))
print()
for i in (l['records']['location'])[0]['weatherElement']:
    print(i)
"""
print()
    
conn = sqlite3.connect('weather.db')
c = conn.cursor()

#創建table叫LOCATION
""""
c.execute('''CREATE TABLE LOCATION
            (locationName TEXT NOT NULL,
            startTime TEXT NOT NULL,
            endTime TEXT NOT NULL,
            parameterName TEXT NOT NULL,
            parameterValue TEXT NOT NULL);
        ''')
conn.commit()
conn.close()
"""

#原本這樣把資料丟進table 但失敗了
"""
for i in l['records']['location']:
    for a in i['weatherElement'][0]['time']:
        c.execute ('INSERT OR REPLACE INTO LOCATION (locationName,startTime,endTime,parameterName,parameterValue) \
        VALUES (i['locationName'], a['startTime'], a['endTime'],a['parameter']['parameterName'],a['parameter']['parameterValue'] )')
"""      



for i in l['records']['location']:
        for a in i['weatherElement'][0]['time']:
                c.execute('INSERT OR REPLACE INTO LOCATION (locationName, startTime, endTime, parameterName, parameterValue) \
                                        VALUES (?,?,?,?,?)', (\
                                        i['locationName'],\
                                        a['startTime'],\
                                        a['endTime'],\
                                        a['parameter']['parameterName'],\
                                        a['parameter']['parameterValue']))
           
conn.commit()        
