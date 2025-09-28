from enum import Enum, auto

class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99

class PaymentError(Exception):
    """Exception raised for payment processing errors."""
    pass

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
    # Validate amount
    if amount <= 0:
        raise PaymentError(f"Invalid payment amount: {amount}. Amount must be positive.")
    
    # Process payment based on payment mode
    if not isinstance(payment_mode, PaymentMode):
        raise PaymentError(f"Unsupported payment mode: {payment_mode}")
    
    # Process payment based on the mode
    if payment_mode == PaymentMode.PAYPAL:
        print(f"Processing PayPal payment of ${amount:.2f}")
        # Future integration with PayPal API would go here
    elif payment_mode == PaymentMode.GOOGLEPAY:
        print(f"Processing GooglePay payment of ${amount:.2f}")
        # Future integration with GooglePay API would go here
    elif payment_mode == PaymentMode.CREDITCARD:
        print(f"Processing CreditCard payment of ${amount:.2f}")
        # Future integration with Credit Card processing API would go here
    else:
        # This shouldn't happen due to the isinstance check, but as a fallback
        raise PaymentError(f"Unsupported payment mode: {payment_mode.value}")
    
    print(f"Payment of ${amount:.2f} via {payment_mode.value} processed successfully!")
    return True
