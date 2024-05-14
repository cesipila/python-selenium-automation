# Created by cesip at 5/10/2024
Feature: Tests for Help page

   Scenario: Verify that current promotions dropdown works
    Given Open Help page for returns
    Then  Verify Returns page is opened
    When Select Help topic Target Account
    Then Verify Create account page is opened


  Scenario: User can select Help topic
    Given Open Help page for returns
    Then  Verify Returns page is opened
    When Select Help topic Promotions & Coupons
    Then Verify Current promotions page is opened
    