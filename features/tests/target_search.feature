# Created by cesip at 4/11/2024
Feature: Search tests
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Target home page
    When Search for shirt
    Then Verify search results are shown for shirt

  Scenario Outline: User can search for a product
    Given Open target home page
    When Search for <item>
    Then Verify search results are shown for <expected_item>
    Examples:
    |item       |expected_item
    |mug        |mug
    |tea        |tea
    |white mug  |white mug

  Scenario: Verify that user can see product name
    Given Open target home page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image