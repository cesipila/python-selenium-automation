# Created by cesip at 4/11/2024
Feature: Check Shopping Cart
  # Enter feature description here

  Scenario: User can verify "Your cart is empty"
    Given Open Target main page
    When Shopping Cart is Open
    Then Verify empty card message
