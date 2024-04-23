Feature: Redo Target Search

  Scenario: User can search for coffee
    Given Open Target page
    When Search for coffee
    Then Verify search results for coffee

  Scenario: User can search for a mug
    Given Open Target page
    When Search for mug
    Then Verify search results for mug

  Scenario: User can search for tea
    Given Open Target page
    When Search for tea
    Then Verify search results for tea