import pymysql 
import re 
class EmployeeDao():
    def connectDb(self):
        conn =pymysql.connect(host="localhost",user="root",passwd="password",db="hemlata")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return cursor
    
