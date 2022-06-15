Feature: Filtering
    Given I Launch chrome browser
    When I Open Qa Recruitment task app 
    And I scroll through to product list section
    * Navigate to the left section of the products

Scenario: Products should be filterable
    * try to filter products
    Then products should be filterable

Scenario: Filter products by multiple categories 
    And try to filter mulitple products 
    Then products should be filterable by multiple products

Scenario: Filter products by single price tag
    And try to filter products by price tag
    Then products should be filtered by single price tag

Scenario: Categories and Price filters can be combined
    And filter products by categories and price
    Then products should be filterable

Scenario: No Results when nothing matches
    And filter products
    * nothing matches the filters selected
    Then I should see No Results displayed

Scenario: Filters should affect pagination
    And filter products
    Then pagination should change based on filter
    

