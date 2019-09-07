from flask import *
import pyrebase
app = Flask(__name__)

config = {
    # paste auth stuff here
}


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def basic():
    return render_template('index.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    unsuccessful = 'Please check your credentials'
    sucessful = 'Login Successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('log.html', s=sucessful)
        except:
            return render_template('log.html', us=unsuccessful)

    return render_template('log.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    unsuccessful = 'Please check your credentials'
    sucessful = 'Login Successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('log.html', s=sucessful)
        except:
            return render_template('log.html', us=unsuccessful)

    return render_template('log.html')



if __name__ == '__main__':
    app.run()
