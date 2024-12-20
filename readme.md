# Flask OAuth and Stripe Integration

A Flask application that implements Google OAuth authentication and Stripe payment integration.

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables:
   - Create a `.env` file with the following variables:
     ```
     STRIPE_API_KEY=your_stripe_api_key
     STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
     GOOGLE_CLIENT_ID=your_google_client_id
     GOOGLE_CLIENT_SECRET=your_google_client_secret
     ```


     
## Getting API Keys

### Google OAuth Setup
1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google+ API
4. Go to Credentials
5. Create an OAuth 2.0 Client ID
6. Add `http://localhost:5000/authorize/google` to the authorized redirect URIs
7. Copy the client ID and client secret to your `.env` file

### Stripe Setup
1. Create a [Stripe account](https://stripe.com)
2. Go to the Stripe Dashboard
3. Get your API keys from the Developers section
4. Copy both the publishable key and secret key to your `.env` file

3. Open `http://localhost:5000` in your browser

## Features

- Google OAuth Sign-in
- Stripe Payment Integration
- Simple HTML interface

## Routes

- `/` - Home page with login and payment options
- `/login/<provider>` - Handles OAuth login
- `/authorize/<provider>` - OAuth callback
- `/checkout` - Initiates Stripe payment
- `/success` - Payment success handler
- `/cancel` - Payment cancellation handler

## Security Note

Never commit your `.env` file or expose your API keys. The `.env` file should be listed in your `.gitignore`.
