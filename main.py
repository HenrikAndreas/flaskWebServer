from flask import Flask, render_template, url_for

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

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", posts=posts)

@app.route('/login')
def login():
    return render_template('login.html', title = 'Login')



if __name__ == "__main__":
    app.run(host="localhost", debug=True)



