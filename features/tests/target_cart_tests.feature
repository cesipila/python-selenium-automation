# Created by cesip at 5/7/2024
Feature: Cart tests

  Scenario: Your cart is empty message is shown
    Given Open Target home page
    When Click on Cart icon
    Then Verify Your cart is empty message is shown

  Scenario: Add a single product to the cart
    Given Open Target home page
    When Search for Coffee
    And Click to add a single product to the cart
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product

  Scenario: Add multiple products to the cart
    Given Open Target home page
    When Search for Coffee
    # And Click to add multiple products to the cart


