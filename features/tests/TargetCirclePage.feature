# Created by cesip at 4/20/2024
Feature: Target Circle page

  Scenario: Count number of benefit cells
    Given Open Target Circle page
    When Verify header is shown
    Then Verify there are 6 benefit cells