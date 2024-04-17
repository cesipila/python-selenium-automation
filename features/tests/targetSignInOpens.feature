# Created by cesip at 4/17/2024
Feature: Sign In
  # Enter feature description here

  Scenario: Logged out user can sign back in
    Given Open Target site page
    When Sign in page is opened
    Then Verify Sign in form opened