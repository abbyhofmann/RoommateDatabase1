from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'go neu'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '001507553'
app.config['MYSQL_DB'] = 'roommatelogin'

mysql = MySQL(app)


# url for login page: http://localhost:5000/roommatelogin
@app.route('/roommatelogin/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
        user = cursor.fetchone()

        if user:
            session['loggedin'] = True
            session['id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('homepage'))
        else:
            msg = 'Login unsuccessful'
    return render_template('login_page.html', msg=msg)


@app.route('/roommatelogin/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/roommatelogin/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and \
            'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        age = request.form['age']
        gender = request.form['gender']
        major = request.form['major']
        description = request.form['description']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()

        if user:
            msg = 'User already has an account'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email entered'
        elif not username or not password or not email:
            msg = 'All fields must be filled out'
        else:
            cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)', (username, password, email, age, gender, major, description))
            mysql.connection.commit()
            msg = 'User successfully registered'

    elif request.method == 'POST':
        msg = 'Must fill in all fields to create account'

    return render_template('register_page.html', msg=msg)


@app.route('/roommatelogin/homepage', methods=['GET', 'POST'])
def homepage():
    if session['loggedin']:

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        if request.method == 'POST' and 'sort-feed' in request.form:
            selected_sort_option = request.form.get('sort-feed')

            if selected_sort_option == 'alphabetical':
                cursor.execute('SELECT * FROM users WHERE username != %s ORDER BY USERNAME', (session['username'],))
                all_users = cursor.fetchall()

            elif selected_sort_option == 'most-recent':
                cursor.execute('SELECT * FROM users WHERE username != %s ORDER BY ID DESC', (session['username'],))
                all_users = cursor.fetchall()

            elif selected_sort_option == 'old-to-young':
                cursor.execute('SELECT * FROM users WHERE username != %s ORDER BY AGE DESC', (session['username'],))
                all_users = cursor.fetchall()

            elif selected_sort_option == 'young-to-old':
                cursor.execute('SELECT * FROM users WHERE username != %s ORDER BY AGE', (session['username'],))
                all_users = cursor.fetchall()

            # mysql.connection.commit()  #todo: is this needed?
        #
        # if request.method == 'POST' and 'filter-feed' in request.form:
        #     selected_filter = request.form.get('filter-feed')
        #
        #     if selected_filter == 'female':
        #         cursor.execute('SELECT * FROM users WHERE gender == %s', 'female')
        #         all_users = cursor.fetchall()
        #
        #     elif selected_filter == 'male':
        #         cursor.execute('SELECT * FROM users WHERE gender == %s', 'male')
        #         all_users = cursor.fetchall()
        #
        #     elif selected_filter == '0-17':
        #         cursor.execute('SELECT * FROM users WHERE age > 0 and age < 18')
        #         all_users = cursor.fetchall()
        #
        #     elif selected_filter == '18-22':
        #         cursor.execute('SELECT * FROM users WHERE age >=18 and age < 23')
        #         all_users = cursor.fetchall()
        #
        #     elif selected_filter == '23-30':
        #         cursor.execute('SELECT * FROM users WHERE age >= 23 and age < 31')
        #         all_users = cursor.fetchall()
        #
        #     elif selected_filter == '31+':
        #         cursor.execute('SELECT * FROM users WHERE age >=31')
        #         all_users = cursor.fetchall()

        else:
            cursor.execute('SELECT * FROM users WHERE username != %s ORDER BY ID', (session['username'],))
            all_users = cursor.fetchall()
            mysql.connection.commit()

        return render_template('homepage.html', username=session['username'], entries=all_users)

    return redirect(url_for('login'))


@app.route('/roommatelogin/view_profile')
def view_profile():
    if session['loggedin']:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE id = %s', (session['id'],))
        user = cursor.fetchone()
        return render_template('view_profile.html', user=user)

    return redirect(url_for('login'))


def edit_profile_html():
    if session['loggedin']:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE id = %s', (session['id'],))
        user = cursor.fetchone()
        return render_template('edit_profile.html',
                               user=user)  # todo: figure out how to switch between html files (adding stuff after return statement)

    return redirect(url_for('login'))


@app.route('/roommatelogin/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    msg = ''
    if session['loggedin']:

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE id = %s', (session['id'],))
        user_to_edit = cursor.fetchone()

        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and \
                'email' in request.form and 'age' in request.form and 'gender' in request.form and 'major' in request.form \
                and 'description' in request.form:
            new_username = request.form['username']
            new_password = request.form['password']  # TODO add constraints for email ... autofill the current table values in the html file
            new_email = request.form['email']
            new_age = request.form['age']
            new_gender = request.form['gender']
            new_major = request.form['major']
            new_description = request.form['description']

            if not re.match(r'[^@]+@[^@]+\.[^@]+', new_email):
                msg = 'Invalid email entered'

            else:
                sql_update = 'UPDATE users SET username=%s, password=%s, email=%s, age=%s, gender=%s, major=%s, description=%s WHERE id=%s'
                values = (new_username, new_password, new_email, new_age, new_gender, new_major, new_description, session['id'])
                cursor.execute(sql_update, values)
                mysql.connection.commit()
                return redirect(url_for('view_profile'))
        elif request.method == 'POST':
            msg = 'All fields must be filled out'

        return render_template('edit_profile.html', user=user_to_edit, msg=msg)

    return redirect(url_for('login'))
# todo : add the else condition
