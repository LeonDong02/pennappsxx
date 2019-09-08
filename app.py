from flask import *
import pyrebase
import json
import requests
import urllib.request
app = Flask(__name__)

with open('config.json') as config_file:
    config = json.load(config_file)

firebaseConfig = config['firebaseConfig']
gsConfig = config['gsConfig']

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

auth_data = {
    'grant_type'    : 'client_credentials',
    'client_id'     : gsConfig['client_id'],
    'client_secret' : gsConfig['client_secret'],
    'scope'         : 'read_content read_financial_data read_product_data read_user_profile'
}

# create session instance
session = requests.Session()

# make a POST to retrieve access_token
auth_request = session.post('https://idfs.gs.com/as/token.oauth2', data = auth_data)
access_token_dict = json.loads(auth_request.text)
access_token = access_token_dict['access_token']

# update session headers
session.headers.update({'Authorization':'Bearer '+ access_token})

# test API connectivity 
request_url = 'https://api.marquee.gs.com/v1/users/self'
gsRequest = session.get(url=request_url)
print(gsRequest.text)


@app.route('/', methods=['GET', 'POST'])
def basic():
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/signin', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return redirect('dashboard')
        except:
            return render_template('log.html', t="Log In", loginFailed=True)

    return render_template('log.html', t="Log In")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            return render_template('log.html', t="Sign Up", signupSuccess=True)
        except:
            return render_template('log.html', t="Sign Up", signupFailed=True)
    return render_template('log.html', t="Sign Up")


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run()
