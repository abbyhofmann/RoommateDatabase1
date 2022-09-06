# import mysql.connector
# from mysql.connector import Error
# from mysql.connector import errorcode
# from passlib.hash import sha256_crypt
#
# try:
#     db_connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="001507553"
#     )
#     print("Connection established")
# except mysql.connector.Error as e:
#     if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Incorrect user or password")
#     else:
#         print(e)
#
# # cursor object
# cursorObject = db_connection.cursor()
#
# # prevents database with an existing name from being added
# cursorObject.execute("DROP database IF EXISTS login")
#
# # creates the database
# cursorObject.execute("CREATE DATABASE login")
#
# cursorObject.execute('USE login')
#
# # creates the table for storing login info
# loginTable = """CREATE TABLE LOGIN (
# id INT AUTO_INCREMENT PRIMARY KEY,
# username VARCHAR(100),
# password VARCHAR(200),
# email VARCHAR(35)
# )
# """
# cursorObject.execute(loginTable)
# db_connection.commit()
#
#
# def insert_login(username, password, email):
#     pswrd = sha256_crypt.hash(password)
#     insert_query = """INSERT INTO login (username, password, email) VALUES (%s, %s, %s)"""
#     insert_data = (username, pswrd, email)
#
#     try:
#         cursorObject.execute(insert_query, insert_data)
#         db_connection.commit()
#         print("table entry committed")
#         if cursorObject.lastrowid:
#             print('last row id', cursorObject.lastrowid)
#         else:
#             print('last insert id not found')
#     except Error as error:
#         print(error)
#         print("!")
#     # finally:
#     #     cursorObject.execute('USE login')
#     #     print("Table entries: ")
#     #     cursorObject.execute('SELECT * FROM LOGIN WHERE username=%s', ('kahof',))
#     #     print(cursorObject.fetchall())
#
#         # db_connection.close()
#         # cursorObject.close()
#
#
# # prints the list of databases in mysql
# # print("List of databases: ")
# # cursorObject.execute("SHOW DATABASES")
# # print(cursorObject.fetchall())
#
#
# def main():
#     insert_login('abbyh', 'abssss', 'hofabby@gmail.com')
#
#
# if __name__ == '__main__':
#     main()
#
#
# # closes the connection
# db_connection.close()
# cursorObject.close()