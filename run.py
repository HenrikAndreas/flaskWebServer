from flask import Flask, render_template, url_for, escape, request, flash, redirect
from forms import Registration, Login # From another python file

posts = [
    {
        'title' : 'Welcome',
        'author' : 'Henrik Andreas',
        'date' : '11.12.2019',
        'content' : 'Here you are able to control parts of my Raspberry Pi, simply because why the fuck not? This is a page with a lot of bullshit, so I hope you will enjoy!'
        },
    {
        'title' : 'Instructions',
        'author' : 'Henrik Andreas',
        'date' : '11.12.2019',
        'content' : 'If you access the "Playground" section you can choose to turn off my lamp!'
    }
]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'pakhoda'

# Adding data from /register, to database after submitting
def addData(name, password, email):
    database = open("database.dat", 'a')
    database.write(f"{name} {password} {email}\n")
    database.close()
# Setting data from database into dictionary
def getData():
    data = {}
    database = open("database.dat", 'r')
    line = database.readline()
    while line != "":
        line = line.lstrip().rstrip().split()
        data[line[0]] = {"password" : line[1], "email" : line[2]}
        line = database.readline()
    return data


        

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login() # Form from the forms.py file
    if form.validate_on_submit():
        data = getData()
        username = form.username.data
        password = form.password.data
        if username in data and data[username]["password"] == password:
            flash(f"You're now logged in {username}", "success")
        else:
            flash(f"Unsuccessful login. Check credentials", "danger")
    return render_template('login.html', title = 'Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        addData(username, password, email)

        flash(f"Sucsessfully created account for {form.username.data}", "success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/features')
def features():
    return render_template('features.html')



#Drafting______________
@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/users/<username>')
def showUser(username):
    return f"{escape(username)}'s profile"



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



