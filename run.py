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

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login() # Form from the forms.py file
    if form.validate_on_submit():
        if form.username.data == "Henrik" and form.password.data == "7mammA99":
            flash(f"You're now logged in {form.username.data}", "success")
            return redirect(url_for('home'))
        else:
            flash(f"Unsuccessful login. Check credentials", "danger")
    return render_template('login.html', title = 'Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
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



