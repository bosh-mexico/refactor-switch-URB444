# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 15:15:14 2025

@author: HUZ1KOR
"""
from checkout_items import PaymentMode

class PaymentError(Exception):
    """Exception raised for payment processing errors."""
    pass

def input_validation(amount,payment_mode):
    if amount<0 or amount==0:
        raise PaymentError(f"Invalid payment amount: {amount}. Amount must greater than 0")

    if not isinstance(payment_mode, PaymentMode):
        raise PaymentError(f"Unsupported payment mode: {payment_mode}")
