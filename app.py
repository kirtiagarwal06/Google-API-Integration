from flask import Flask, redirect, url_for, session, jsonify, render_template
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
import os
import pickle

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'  # Replace with a secret key for session management

# OAuth 2.0 client setup
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # For development only
CLIENT_SECRETS_FILE = 'client_secrets.json'
SCOPES = ['https://www.googleapis.com/auth/business.manage']
REDIRECT_URI = 'http://localhost:5000/callback'

flow = Flow.from_client_secrets_file(
    CLIENT_SECRETS_FILE,
    scopes=SCOPES,
    redirect_uri=REDIRECT_URI
)

@app.route('/')
def index():
    if 'credentials' not in session:
        return redirect(url_for('login'))
    credentials = pickle.loads(session['credentials'])
    service = build('mybusinessbusinessinformation', 'v1', credentials=credentials)
    # Example API call to list locations (requires additional setup in your project)
    # locations = service.accounts().locations().list(parent='accounts/YOUR_ACCOUNT_ID').execute()
    return render_template('index.html')

@app.route('/login')
def login():
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    session['state'] = state
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not flow.credentials:
        return 'Authentication failed', 401

    session['credentials'] = pickle.dumps(flow.credentials)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('credentials', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
