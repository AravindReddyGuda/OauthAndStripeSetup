import os
from flask import Flask, render_template_string
from oauth_google import setup_oauth, login, authorize
from stripe_payment import create_checkout_session, success, cancel

app = Flask(__name__)
app.secret_key = os.getenv('83938393', 'your-default-secret-key')  

# Add these lines to set up the Google OAuth configuration
app.config['GOOGLE_CLIENT_ID'] = os.getenv('GOOGLE_CLIENT_ID')
app.config['GOOGLE_CLIENT_SECRET'] = os.getenv('GOOGLE_CLIENT_SECRET')

# Setup OAuth (Google login)
setup_oauth(app)

# HTML Template for login and payment page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup Page</title>
</head>
<body>
    <h1>Sign Up Using:</h1>
    <ul>
        <li><a href="{{ url_for('handle_login', provider='google') }}">Google</a></li>
    </ul>
    <br><br>
    <h2>Payment</h2>
    <button onclick="location.href='{{ url_for('checkout') }}'">Pay with Stripe</button>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login/<provider>')
def handle_login(provider):
    return login(provider)

@app.route('/authorize/<provider>')
def handle_authorize(provider):
    return authorize(provider)

@app.route('/checkout')
def checkout():
    return create_checkout_session()

@app.route('/success')
def handle_success():
    return success()

@app.route('/cancel')
def handle_cancel():
    return cancel()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
