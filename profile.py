class Profile:

    def __init__(self, usern, name, age, gen, maj, desc):
        self.username = usern
        self.name = name
        self.age = age
        self.gender = gen
        self.major = maj
        self.description = desc

    def get_username(self):
        return self.username

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_major(self):
        return self.major

    def get_description(self):
        return self.description



# original main.py file
# from flask import Flask, render_template, request, session, flash
# from passlib.hash import sha256_crypt
#
# import mysql.connector
# import os
#
# app = Flask(__name__)
#
# connect = mysql.connector.connect(
#     user='root',
#     password='001507553',
#     database='login'
# )
#
#
# @app.route('/')
# def start():
#     if not session.get('logged_in'):
#         return render_template('login_page.html')
#     else:
#         return render_template('logged_in_page.html')
#
#
# @app.route('/login', methods=['POST'])
# def user_login():
#     login = request.form
#
#     username = login['username']
#     password = login['password']
#
#     cursor = connect.cursor(buffered=True)
#     # selects the table entry that corresponds to the username
#     data = cursor.execute('SELECT * FROM login WHERE username=%s', username)
#     # retrieves the password associated with the username
#     data = cursor.fetchall()[2]
#
#     # verify the typed password matches the one stored in the table
#     if sha256_crypt.verify(password, data):
#         profile = True
#
#     if profile:
#         session['logged_in'] = True
#     else:
#         flash('incorrect password!')
#     return start()
#
#
# @app.route('logout')
# def logout():
#     session['logged_in'] = False
#     return start()
#
#
# if __name__ == "__main__":
#     app.secret_key = os.urandom(12)
#     app.run(debug=False, host='0.0.0.0', port=5000)
