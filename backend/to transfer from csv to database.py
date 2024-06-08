import mysql.connector
import csv

mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE SMARTDESTINA")
mycursor.execute("USE SMARTDESTINA")

f1 = open('data.csv', 'r')
allrec = csv.reader(f1)
header_row = next(allrec)
column_definitions = []
col_name=header_row[0]
column_definitions.append(f"{col_name} int(10)")
for i in range(1,8):
     col_name=header_row[i]
     column_definitions.append(f"{col_name} varchar(100)")
for i in range(8,12):
     col_name=header_row[i]
     column_definitions.append(f"{col_name} decimal(10,4)")
sql_stmt = "CREATE TABLE DATA ( " + ", ".join(column_definitions) + " )"
mycursor.execute(sql_stmt)
mycursor.execute("ALTER TABLE data ADD PRIMARY KEY(name)")
mydb.commit()
f1.close()
f1 = open('data.csv', 'r')
allrec = csv.reader(f1)
header_row = next(allrec)
for rec in allrec:
     column_definitions = []
     col_name=int(rec[0])
     column_definitions.append(f"{col_name}")
     for i in range(1,8):
          col_name="'"+rec[i]+"'"
          column_definitions.append(f"{col_name}")
     for i in range(8,12):
          col_name=float(rec[i])
          column_definitions.append(f"{col_name}")
     sql_stmt = "INSERT INTO DATA VALUES ( " + ", ".join(column_definitions) + " );"
     mycursor.execute(sql_stmt)
mydb.commit()
f1.close()

f1 = open('footfall data.csv', 'r')
allrec = csv.reader(f1)
header_row = next(allrec)
column_definitions = []
col_name=header_row[0]
column_definitions.append(f"{col_name} int(10)")
col_name=header_row[1]
column_definitions.append(f"{col_name} varchar(100)")
for i in range(2,14):
     col_name=header_row[i]
     column_definitions.append(f"{col_name} int(10)")
col_name=header_row[14]
column_definitions.append(f"{col_name} decimal(10,5)")
sql_stmt = "CREATE TABLE FDATA ( " + ", ".join(column_definitions) + " )"
mycursor.execute(sql_stmt)
mycursor.execute("ALTER TABLE fdata ADD PRIMARY KEY(name)")
mydb.commit()
f1.close()
f1 = open('footfall data.csv', 'r')
allrec = csv.reader(f1)
header_row = next(allrec)
for rec in allrec:
     column_definitions = []
     col_name=int(rec[0])
     column_definitions.append(f"{col_name}")
     col_name="'"+rec[1]+"'"
     column_definitions.append(f"{col_name}")
     for i in range(2,14):
          col_name=int(rec[i])
          column_definitions.append(f"{col_name}")
     col_name=float(rec[14])
     column_definitions.append(f"{col_name}")
     sql_stmt = "INSERT INTO FDATA VALUES ( " + ", ".join(column_definitions) + " );"
     mycursor.execute(sql_stmt)
mydb.commit()
f1.close()
