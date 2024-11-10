import pymysql

dataBase = pymysql.connect(
    host="localhost",
    user="root",
    password="Aizen$33"
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("Created")
