Feature: Target Search Outline

  Scenario Outline: User can search for a products
    Given Open Target page
    When Search for <item>
    Then Verify search results for <expected_item>
    Examples:
    |item         |expected_item
    |mug          |mug
    |cat          |cat
    |shirt        |shirt
    |soup         |soup
