
import importlib
checkout_module = importlib.import_module("checkout_items")
validation_module = importlib.import_module("validate_inputs")

class PaymentProcessor:
    def __init__(self, payment_mode, amount):
        self.payment_mode = payment_mode
        self.amount = amount

    def process(self):
        processors = {
            "PAYPAL": self.process_using_paypal,
            "GOOGLEPAY": self.process_using_gpay,
            "CREDITCARD": self.process_using_credit
        }
        processor = processors.get(self.payment_mode.name, self.process_default)
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
        raise validation_module.PaymentError(f"Unsupported payment mode: {self.payment_mode.name}")
