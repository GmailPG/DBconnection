import cx_Oracle
import csv

## To connect to DB##
dsnStr = cx_Oracle.makedsn("illnqw1864", "1521", "CMDDB1864")
db = cx_Oracle.connect(user="ABPAPP1", password="ABPAPP1", dsn=dsnStr)
cursor = db.cursor()
### DB##
## Fetching row id from table##

SQL = "DROP TABLE APE1_BACKUP_EVENT"
cursor.execute(SQL)

SQL1 = "CREATE table APE1_BACKUP_EVENT ( customer_id VARCHAR(20))"
cursor.execute(SQL1)

SQL2 = "SELECT nvl(max(rownum)+1,1) from APE1_BACKUP_EVENT"
cursor.execute(SQL2)
rownum=cursor.fetchone()
x=rownum[0]
#######
## working on csv file ##

path = r'C:\Users\parulgu\Desktop\cust.csv'
with open(path, newline='') as csvfile:
    record = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for var1 in record:
        print(var1)
        sqlquery = "INSERT INTO APE1_BACKUP_EVENT VALUES (%s)" % (var1[0])
        cursor.execute(sqlquery)
db.commit()
