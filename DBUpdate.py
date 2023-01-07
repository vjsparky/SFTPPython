import mysql.connector

def DBTableupdate(Filename, status, Submitdate):
    try : 
        mydb = mysql.connector.connect(host="localhost", user="root", password="Sparky@6@21998")
        mycursor = mydb.cursor()
        sql = "INSERT INTO vijay.sftpaudit (Filename, status, Submitdate ) VALUES (%s, %s, %s)"
        val = (Filename, status, Submitdate)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Successfully updated Status message in the DB Table ")
    except Exception as e :
        print("Unable to update in the DB Table..", e)

