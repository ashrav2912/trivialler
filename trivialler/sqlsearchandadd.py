import mysql.connector
import os
# Connect to database
password = os.getenv('SQL_PWD')
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=password,
    database="travel_db"
    )

mycursor = mydb.cursor(buffered=True)
mycursor.execute("USE travel_db")

def sqlsearch(city_name):
    sql = "SELECT * FROM travel_table WHERE city_name = %s"
    adr = (city_name, )
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchmany(5)
    for x in myresult:
        print(x)
    return myresult

def sqladd(city_name, from_date, to_date, hotel_name, review):
    sqlverify = "SELECT * FROM travel_table WHERE review = %s"
    valverify = (review, )
    mycursor.execute(sqlverify, valverify)
    mycursor.fetchall()
    if mycursor.rowcount > 0:
        print("Review already exists.")
        return
    sql = "INSERT INTO travel_table (city_name, from_date, to_date, hotel_name, review) VALUES (%s, %s, %s, %s, %s)"
    val = (city_name, from_date, to_date, hotel_name, review)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")