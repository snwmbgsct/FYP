

import pymysql

conn = pymysql.connect(
    host="192.168.20.215",
    
    user="root",
    password="",
    db="fypdatabase")


cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = "select * from main where Sid=21"
cursor.execute(sql)


result = cursor.fetchall()
cursor.close()
conn.close()


SpHmin = float(result[0]['SpHmin'])
SpHmax =  float(result[0]['SpHmax'])

Tge_min = float(result[0]['Tge_min (℃)'])
Tge_max= float(result[0]['Tge_max (℃)'])

Tgr_min = float(result[0]['Tge_min (℃)'])
Tgr_max= float(result[0]['Tge_max (℃)'])

SRAH_min = float(result[0]['SRAH_min (%)'])
SRAH_max= float(result[0]['SRAH_max (%)'])

SRSH_min = float(result[0]['SRAH_min (%)'])
SRSH_max= float(result[0]['SRAH_max (%)'])



