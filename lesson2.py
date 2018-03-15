import cx_Oracle

dsnStr = cx_Oracle.makedsn("illnqw1864", "1521", "CMDDB1864")
db = cx_Oracle.connect(user="ABPAPP1", password="ABPAPP1", dsn=dsnStr)
cursor = db.cursor()
#SQL1 = "CREATE table APE1_BACKUP_EVENT ( customer_id VARCHAR(20) DEFAULT NULL)"
#cursor.execute(SQL1)

SQL = "SELECT * FROM ape1_rated_event"
cursor.execute(SQL)
for record in cursor:
  print(record)