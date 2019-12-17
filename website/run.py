from flask import Flask, redirect, make_response, render_template, request, url_for, flash, Response
from forms import Login, Lamp
import os
import cv2
# import RPi.GPIO as GPIO

# # Pin from which we'll output voltage
# channel = 18

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(channel, GPIO.OUT) # Defining specified channel as an output pin

# def lampOn(pin):
#         GPIO.output(pin, GPIO.HIGH)

# def lampOff(pin):
#         GPIO.output(pin, GPIO.LOW)


#Fix url_for('lamp') in layout.html and lamp route


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)
cam = cv2.VideoCapture(0) # For livestream
# app.secret_key = os.urandom(16) #?

posts = [
    {
        'title' : 'Welcome',
        'author' : 'Henrik Andreas',
        'date' : '16.12.2019',
        'content' : 'Welcome to my webpage, which is full of bullshit. On the playground you might be able to have some fun'
    }
]

# Opens userdata.dat and extracts the data to
# a dictionary --> userData = {username : {password:'password', id:'id'} }
def getUserData():
    dataFile = open('userdata.dat', 'r')
    userData = {}
    line = dataFile.readline()
    while line != "":
        line = line.rstrip().lstrip().split('|')
        userData[line[0]] = {'password':line[1], 'id' : line[2]}
        line = dataFile.readline()
    return userData

# Before accessing anything, one must log in
@app.route('/')
@app.route('/login', methods=['GET'])
def login():
    form = Login()
    return render_template('login.html', form=form, title='Login')

# Post method to verify the login credentials
@app.route('/verification', methods=['POST'])
def verification():
    userData = getUserData()
    user = request.form['username']
    password = request.form['password']
    if user in userData:
        if password == userData[user]['password']:
            response = make_response(redirect(url_for('home', username=user)))
            response.set_cookie('id', userData[user]['id'])
            return response
    return redirect('login')

# Checks if username matches the user's cookie, in order to access
@app.route('/<username>/home', methods=["GET"])
def home(username):
    userData = getUserData()
    idCookie = request.cookies.get('id')
    if userData[username]['id'] == idCookie:
        return render_template('home.html', title='Home', username=username, posts=posts)
    return "Access denied"

# Lamp site. Here you can turn off lamp
@app.route('/<username>/lamp', methods=["GET"])
def lamp(username):
    form = Lamp()
    userData = getUserData()
    idCookie = request.cookies.get('id')
    if userData[username]['id'] == idCookie:
        return render_template('lamp.html', title='Lamp', username=username, form=form)
    return 'Access denied'

#Livestream test
def gen():
   while True: 
      rval, frame = cam.read()
      cv2.imwrite('pic.jpg', frame)
      yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + open('pic.jpg', 'rb').read() + b'\r\n')

@app.route('/video_feed') 
def video_feed(): 
   return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
# Livestream test over

# POST site, verifying data and turning on / off lamp
@app.route('/<username>/lampverification', methods=['POST'])
def lampverification(username):
    userData = getUserData()
    idCookie = request.cookies.get('id')
    if userData[username]['id'] == idCookie:
        if request.form.get('value') == '1' :
            print("Lamp on")
        elif request.form.get('value') == '0' :
            print("Lamp off")
        # if (request.form.get('value')) == '0' : lampOn(channel)
        # elif (request.form.get('value')) == '1' : lampOff(channel)
    return redirect(url_for('lamp', username=username))
    
if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, threaded=True)


# terminal with requests
# >>> xID = requests.post('http://127.0.0.1:5000/verification', {'username' : 'henrik', 'password' : '123'} )
# >>> xID
# <Response [200]>
