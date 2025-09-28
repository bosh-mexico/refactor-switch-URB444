# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 15:13:41 2025

@author: HUZ1KOR
"""
from enum import Enum
import validate_inputs
from process_payment import PaymentProcessor

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
    validate_inputs.validate_amount(amount)
    validate_inputs.validate_payment_mode(payment_mode)

    # Create payment processor and process payment
    processor = PaymentProcessor(payment_mode, amount)
    result = processor.process()

    print(f"Payment of ${amount:.2f} via {payment_mode.name} processed successfully!")
    return result
