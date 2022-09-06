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
# loginTable = """CREATE TABLE LOGIN (
# id INT AUTO_INCREMENT PRIMARY KEY,
# username VARCHAR(25),
# password VARCHAR(25),
# email VARCHAR(35)
# )
# """
# cursorObject.execute(loginTable)
# database.commit()
#
# database.close()
