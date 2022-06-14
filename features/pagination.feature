Feature: Add to Cart
    Background: Web App Launch
        Given I Launch chrome browser
        When I Open Qa Recruitment task app  

    Scenario: Pagination
        And I scroll to the bottom of product list section
        Then I should find product pagination

    Scenario: Items per Page
        And I scroll to the product list section
        * Navigate through different pages 
        Then I should find six products per page

    Scenario: Show current page
        And I scroll to the bottom of product list section
        * navigate through the different pages
        Then I should see the current page displayed

    Scenario: Previous Button on First Page
        And I scroll to the bottom of product list section
        * I am on the first page of the product list
        Then Previous Button should not be displayed

    Scenario: Next Button on Last Page
        * Navigate to the last page under pagination
        Then Next Button should not be displayed        
