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
    """
    # Validate inputs
    validate_inputs.input_validation(amount, payment_mode)

    # Create payment processor and process payment
    processor = PaymentProcessor(payment_mode, amount)
    result = processor.process()

    print(f"Payment of ${amount:.2f} via {payment_mode.name} processed successfully!")
    return result
