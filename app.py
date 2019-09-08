from flask import *
import pyrebase
import json
import requests
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
    unsuccessful = 'Please check your credentials'
    successful = 'Login Successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('members.html', s=successful)
        except:
            return render_template('log.html', t="Log In", us=unsuccessful)

    return render_template('log.html', t="Log In")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        user = auth.create_user_with_email_and_password(email, password)
    return render_template('log.html', t="Sign Up")


@app.route('/members', methods=['GET', 'POST'])
def members():
    return render_template('members.html')


if __name__ == '__main__':
    app.run()
