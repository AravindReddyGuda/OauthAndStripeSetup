import os
import stripe
from flask import redirect, url_for
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Stripe
stripe.api_key = os.getenv('STRIPE_API_KEY')

def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Subscription',
                    },
                    'unit_amount': 2000,  # $20.00
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('handle_success', _external=True),
            cancel_url=url_for('handle_cancel', _external=True),
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return str(e)

def success():
    return "Payment Successful! Thank you for your purchase."

def cancel():
    return "Payment Cancelled. Please try again."
