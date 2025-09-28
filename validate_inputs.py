
import importlib
checkout_module = importlib.import_module("checkout_items")

class PaymentError(Exception):
    """Exception raised for payment processing errors."""
    pass

def validate_amount(amount):
    if amount<0 or amount==0:
        raise PaymentError(f"Invalid payment amount: {amount}. Amount must greater than 0")

def validate_payment_mode(payment_mode):
    try:
        checkout_module.PaymentMode(payment_mode.value)
    except:
        raise PaymentError(f"Unsupported payment mode: {payment_mode}")

