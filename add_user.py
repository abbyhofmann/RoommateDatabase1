# from flask import Flask, render_template, request
# from passlib.hash import sha256_crypt
# import mysql.connector
#
# app = Flask(__name__)
#
# connector = mysql.connector.connect(
#     user='root',
#     password='001507553',
#     database='login'
# )
#
#
# @app.route('/')
# def index():
#     username = "abbyh"
#     password = sha256_crypt.hash("password")
#     email = "abbyh@gmail.com"
#
#     cursor = connector.cursor()
#     cursor.execute('INSERT INTO login (username, password, email) VALUES (%s, %s, %s)', (username, password, email))
#     connector.commit()
#     cursor.close()
#
#     return "New user added"
#
#
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port='5000')
