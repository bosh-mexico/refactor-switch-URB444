# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 15:43:32 2025

@author: HUZ1KOR
"""
from checkout_items import PaymentMode
from validate_inputs import PaymentError

class PaymentProcessor:
    def __init__(self, payment_mode, amount):
        self.payment_mode = payment_mode
        self.amount = amount

    def process(self):
        processors = {
            PaymentMode.PAYPAL: self.process_using_paypal,
            PaymentMode.GOOGLEPAY: self.process_using_gpay,
            PaymentMode.CREDITCARD: self.process_using_credit
        }
        processor = processors.get(self.payment_mode, self._process_default)
        return processor(self.amount)

    def process_using_paypal(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f}")
        # Add PayPal-specific logic here
        return True

    def process_using_gpay(self, amount):
        print(f"Processing GooglePay payment of ${amount:.2f}")
        # Add GooglePay-specific logic here
        return True

    def process_using_credit(self, amount):
        print(f"Processing CreditCard payment of ${amount:.2f}")
        # Add Credit Card-specific logic here
        return True

    def process_default(self, amount):
        raise PaymentError(f"Unsupported payment mode: {self.payment_mode.name}")
