Feature: Payment Processing System
  As a customer
  I want to checkout using different payment methods
  So that I can complete my purchase conveniently

  Scenario Outline: Checkout with supported payment modes
    Given the customer has items in their cart
    And the payment amount is <amount>
    When the customer selects <payment_mode> as the payment mode
    Then the system should process the payment successfully
    And a confirmation message should be displayed with <payment_mode> and <amount>

    Examples:
      | payment_mode | amount  |
      | PaymentMode.PAYPAL       | 100.50  |
      | PaymentMode.GOOGLEPAY    | 75.25   |
      | PaymentMode.CREDITCARD   | 250.00  |

  Scenario: Checkout with unsupported payment mode
    Given the customer has items in their cart
    And the payment amount is 150.75
    When the customer selects an unsupported payment mode
    Then the system should handle the error gracefully
    And an error message should be displayed about invalid payment mode

  Scenario: Checkout with zero amount
    Given the customer has items in their cart
    And the payment amount is 0.00
    When the customer selects GooglePay as the payment mode
    Then the system should handle the error gracefully
    And an error message should be displayed about invalid amount
    
  Scenario: Checkout with negative amount
    Given the customer has items in their cart
    And the payment amount is -10.00
    When the customer selects PayPal as the payment mode
    Then the system should handle the error gracefully
    And an error message should be displayed about invalid amount
