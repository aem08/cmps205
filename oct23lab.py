import pyodbc
server = 'alexasql.database.windows.net'
database = 'AdventureWorks2016'
username = 'cmps253'
password = 'Cmps205!'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT top 10 * from Person.Person ")
row = cursor.fetchone()
lst=[]
while row:
   lst.append((row[4]))
   print(row[4]+' '+row[6])
   row = cursor.fetchone()
user_input=int(input('Which row do you want to see? '))
firstname=lst[user_input]
print(firstname)
cursor.execute("SELECT * from Person.Person where firstname='%s'"%firstname)
row=cursor.fetchone()
while row:
    print(row[4])
    row=cursor.fetchone()

    
