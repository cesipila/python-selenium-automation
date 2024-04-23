# Created by cesip at 4/22/2024
Feature: Target Cart Tests

  Scenario: 'Your cart is empty' message is shown
    Given Open target main page
    When Click on Cart icon
    Then Verify your cart is empty message is shown


  Scenario: User can add a product to cart
    Given Open target main page
    When Search for coffee
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product
