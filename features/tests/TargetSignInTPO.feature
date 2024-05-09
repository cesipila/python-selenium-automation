# Created by cesip at 5/8/2024
Feature: Sign In Features

  Scenario: Verify that logged out user can access Sign In
    Given Open Target home page
    When Click sign in from main page
    And Click sign in from side navigation page
    Then Verify sign in form opened

# You can generate a fake email: email-fake.com
  Scenario: Verify that logged out user can access Sign In
    Given Open Target home page
    When Click sign in from main page
    And Click sign in from side navigation page
    And Input email anvarv@btcmod.com
    And Input password testpassword1234
    And Click sign in from sign in page
    Then Verify user is logged in