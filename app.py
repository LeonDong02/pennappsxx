from flask import *
import pyrebase
import json
import requests
app = Flask(__name__)

with open('config.json') as config_file:
    config = json.load(config_file)

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

auth_data = {
    'grant_type'    : 'client_credentials',
    'client_id'     : client_id,
    'client_secret' : client_secret,
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
request = session.get(url=request_url)
print(request.text)


@app.route('/', methods=['GET', 'POST'])
def basic():
    return render_template('index.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    unsuccessful = 'Please check your credentials'
    successful = 'Login Successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('log.html', t="Log In", s=successful)
        except:
            return render_template('log.html', t="Log In", us=unsuccessful)

    return render_template('log.html', t="Log In")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    unsuccessful = 'Please check your credentials'
    successful = 'Login Successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('log.html', t="Sign Up", s=successful)
        except:
            return render_template('log.html', t="Sign Up", us=unsuccessful)

    return render_template('log.html', t="Sign Up")



if __name__ == '__main__':
    app.run()
