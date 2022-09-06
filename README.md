# Roommate Database Web Application  

**Description**<br /> 
- This is a simple web application based off a roommate database. The database, created 
using MySQL, stores user profiles in a table. Each user profile consists of a username, 
password, email address, age, gender, major, and short personal description. The 
program allows a user to login, permitted they have an account, or register if the user 
does not have an existing account. Once logged in, the homepage displays the 
profiles of the other registered users as the "feed" of the application. These results 
can be sorted alphabetically, oldest-to-youngest by age, youngest-to-oldest by age, 
and by newest-to-oldest profiles. The results can also be filtered by gender (male and 
female) or age (based of various ranges). The logged in user also has the ability to 
view their own profile and update the various entires if needed. A logout button returns 
the user to the login/register page. 
- I was motivated to build this program as a way to explore an interest in practical 
programming applications. On Northeastern's Reddit page, I oftentimes see students 
seeking roomates or housing. A Northeastern-specific roommate search application does 
not currently exist, so I used its absence as a starting point for learning more 
about databases and web-based applications. 
- I utilized MySQL, Python, and HTML to complete this application. To expand upon this 
project, I would improve the styling and appearance of the program using CSS and/or 
Javascript. I would also add additional features to make the program more realistic, 
such as a way for users to interact with each other via messaging or some other means. 
I would eventually like to publicly host my webiste instead of simply using localhost. 
- The most challening part of this project was learning how to connect HTML, Python, 
and MySQL. I didn't have too much experience with HTML, Python, or MySQL, but I 
learned more about connecting front-end code with back-end code to make an 
application complete.  

**Installation**<br />
- This program does not require installation. 

**How to Use**<br />
- To use, open the command prompt/terminal on your machine. Navigate to the project 
folder. In the command line, run the following commands: 
    set FLASK_APP=main.py 
    set FLASK_DEBUG=1 
    flask run 
- Open a browser and access the application via http://localhost:5000/roommatelogin/

