Feature: Sorting
    Background: Web App Launch
        Given I Launch chrome browser
        When I Open Qa Recruitment task app 
        And I scroll through to product list section
        * Navigate to sort by 
    
    Scenario: Two Types of Sorting
        And click on the dropdown
        Then I should see two options, alphabetically and price

    Scenario: Arrows change the order of Sorting
        And click on the up or down arrow 
        Then sorting should be ascending or descending
