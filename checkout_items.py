# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 15:13:41 2025

@author: HUZ1KOR
"""

from enum import Enum
import importlib
validation_module = importlib.import_module("validate_inputs")
payment_module = importlib.import_module("process_payment")

class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99

def checkout(payment_mode: PaymentMode, amount: float) -> bool:
    """
    Process a payment using the specified payment mode and amount.

    Args:
        payment_mode: The payment mode to use
        amount: The amount to be processed

    Returns:
        True if payment was successful

    Raises:
        PaymentError: If payment mode is invalid or amount is not positive
    """
    # Validate inputs
    validation_module.validate_amount(amount)
    validation_module.validate_payment_mode(payment_mode)

    # Create payment processor and process payment
    processor = payment_module.PaymentProcessor(payment_mode, amount)
    result = processor.process()

    print(f"Payment of ${amount:.2f} via {payment_mode.name} processed successfully!")
    return result
