import pymysql
conn=pymysql.connect(host="localhost",user="root",passwd="root",db="hemlata")

mycur=conn.cursor()

#Create
try:
mycur.execute("CREATE TABLE DemoTb( PersonID int, LastName varchar(255), FirstName varchar(255), Address varchar(255),City varchar(255));")
print("databse created\n")
except:
    print("Table already exists")

#Insert
print("enter data to iinsert into table")
pid=input("Enter person ID: ")
fname=input("Enter First Name: ")
lname=input("Enter Last Name: ")
addr=input("Enter Address: ")
city=input("Enter city: ")
print("INSERT INTO DemoTb values("+pid+',"'+fname+'","'+lname+'","'+addr+'","'+city+'");'"")
mycur.execute("INSERT INTO DemoTb values("+pid+',"'+fname+'","'+lname+'","'+addr+'","'+city+'");'"")
conn.commit()
print("Data inserted\n")


mycur.execute("select * from DemoTb")
conn.commit()

#Delete
#Delete from DemoTb where name='hemlata'
mycur.execute("Delete from DemoTb where City ='Nashik';")
print("row deleted \n\n")
conn.commit()


#Update
#UPDATE table_name SET field1 = new-value1, field2 = new-value2 [WHERE Clause]
mycur.execute("UPDATE DemoTb SET City = 'Pune' Where City='Nashik'")
print("table updated")
conn.commit()
mycur.close()