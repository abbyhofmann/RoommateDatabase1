# import mysql.connector
#
# # connects to database
# database = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="001507553",
#     database="login"
# )
#
# # cursor object
# cursorObject = database.cursor()
#
# # creates the table for storing login info
# profileTable = """CREATE TABLE PROFILES (
# id INT PRIMARY KEY,
# username VARCHAR(25),
# name VARCHAR(25),
# age INT,
# gender CHAR(1),
# major VARCHAR(50),
# description VARCHAR(1000)
# )
# """
# cursorObject.execute(profileTable)
# database.commit()
#
# database.close()
