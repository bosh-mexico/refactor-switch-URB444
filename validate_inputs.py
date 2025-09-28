# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 15:15:14 2025

@author: HUZ1KOR
"""
from checkout_items import PaymentMode

class PaymentError(Exception):
    """Exception raised for payment processing errors."""
    pass

def validate_amount(amount):
    if amount<0 or amount==0:
        raise PaymentError(f"Invalid payment amount: {amount}. Amount must greater than 0")

def validate_payment_mode(payment_mode):
    if not isinstance(payment_mode, PaymentMode):
        raise PaymentError(f"Unsupported payment mode: {payment_mode}")
