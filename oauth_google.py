from flask import redirect, session, url_for
from authlib.integrations.flask_client import OAuth

oauth = OAuth()
google = None

def setup_oauth(app):
    global google
    google = oauth.register(
        name='google',
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_params=None,
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        client_kwargs={'scope': 'openid email profile'}
    )
    oauth.init_app(app)

def login(provider):
    if provider == 'google':
        return google.authorize_redirect(url_for('handle_authorize', provider='google', _external=True))
    return 'Unsupported provider'

def authorize(provider):
    if provider == 'google':
        token = google.authorize_access_token()
        resp = google.get('userinfo')
        user_info = resp.json()
        session['email'] = user_info['email']
        return redirect('/')
    return 'Unsupported provider'
