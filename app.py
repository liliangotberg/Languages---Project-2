"""    # Steps to create a Website using Python Flask
    https://code.visualstudio.com/docs/python/tutorial-flask
    https://richmond.bootcampcontent.com/Richmond-Boot-Camp/UR-RICH-DATA-PT-01-2020-U-C/blob/master/10-Advanced-Data-Storage-and-Retrieval/3/Activities/10-Ins_Flask_with_ORM/Solved/app.py
1. Create a Flask folder on Desktop
2. Open Text Editor, VSC in this example
3. In command line, you can open Flask folder
4. Create a virtual environment named env by entering "python -m venv env", 
    in Mac enter sudo apt-get install python3-venv python3 -m venv env
    OR
    In VSC you can create a virtual environment by opening Command Palette, 
    selecting Python: Select Interpreter, then selecting option with (venv wording). 
    New folders and subfolder will appear in sidebar and the selected environment 
    appears on the left side of the VS Code status bar.
5. Install Flask by entering "pip install flask" in command line
6. Create a new file, app.py to add code (THIS FILE)
7. Write code and follow steps below, save file()
8  In the terminal venv, enter "python -m flask run"
9. Run Code - see environmenta text noting default browse to the rendered page 
    Ctrl+click or copy  url http://127.0.0.1:5000/ and paste it in an empty URL box
10. See your WebPage populate in a virtual environment. 
"""

# import flask micro framework for web applications 
# see route 3 for explanation of redirect and url_for
# (basics-  URL routing and page rendering)

from flask import Flask, redirect, url_for

#  create instance of a flask web application
app = Flask(__name__)

# create first flask decorator "app.route" to map the URL route "/" to a function that returns content. 
# we can have multiple decorators on the same function, one per line to designate routes mapped to the same function.    
# we define how we will reference each page on website 

# first decoder is def home(). it will be the home page - home() is function
# return states what will be displayed in the page
# return is where we can enter html code to display, add a link, write a header
# run code - Hello! This is the main page and then in large text you see HELLO
@app.route("/") 
def home(): 
    return "Hello! This is the main page <h1>HELLO<h1>" 

# second decoder/ another page - is def user(name). user is function
# The value ("/<name>") entered is going to grab that "string" and pass it to my 
## function "user" as a parameter -  
# return states what will be displayed in the page using string format  
# run code - Hello name
@app.route("/<string>")
def user(name):
    return f'Hello {name}'

# third decoder/ last page - is def admin. admin is function
# page will redirect user to another page, in this case, back to home page
# define admin() function 
# return by redirect(ing)(ur_for("home") to home funtion
# url_for is the funtion 

@app.route("/admin")
def admin():
    return redirect(url_for("home")) 

if __name__ == "__main__": # #3 -
    app.run()