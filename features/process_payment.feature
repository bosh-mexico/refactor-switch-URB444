from behave import given, when, then
from payment_processor import PaymentMode, checkout, PaymentError

@given('the customer has items in their cart')
def step_impl(context):
    # This is just a placeholder step for readability
    # In a real implementation, we might set up a cart object
    context.cart_has_items = True

@given('the payment amount is {amount}')
def step_impl(context, amount):
    context.payment_amount = float(amount)

@when('the customer selects {payment_mode} as the payment mode')
def step_impl(context, payment_mode):
    try:
        context.payment_mode = PaymentMode(payment_mode)
    except ValueError:
        context.payment_mode = payment_mode  # Store as string for error testing

@when('the customer selects an unsupported payment mode')
def step_impl(context):
    context.payment_mode = "BitCoin"  # An unsupported payment mode

@then('the system should process the payment successfully')
def step_impl(context):
    try:
        result = checkout(context.payment_mode, context.payment_amount)
        context.payment_result = result
        context.error = None
    except PaymentError as e:
        context.payment_result = False
        context.error = str(e)

@then('a confirmation message should be displayed with {payment_mode} and {amount}')
def step_impl(context, payment_mode, amount):
    # This step would check that the right confirmation message was displayed
    # In a real implementation, we might capture stdout or check a response object
    assert context.payment_result is True, f"Payment failed: {context.error}"
    assert context.error is None, f"Unexpected error: {context.error}"

@then('the system should handle the error gracefully')
def step_impl(context):
    try:
        checkout(context.payment_mode, context.payment_amount)
        assert False, "Expected an error but none occurred"
    except PaymentError:
        # Expected error, test passes
        pass

@then('an error message should be displayed about invalid payment mode')
def step_impl(context):
    try:
        checkout(context.payment_mode, context.payment_amount)
        assert False, "Expected an error about invalid payment mode but none occurred"
    except PaymentError as e:
        assert "Unsupported payment mode" in str(e), f"Unexpected error message: {e}"

@then('an error message should be displayed about invalid amount')
def step_impl(context):
    try:
        checkout(context.payment_mode, context.payment_amount)
        assert False, "Expected an error about invalid amount but none occurred"
    except PaymentError as e:
        assert "Invalid payment amount" in str(e), f"Unexpected error message: {e}"
