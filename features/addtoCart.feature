Feature: Add to Cart
    Background: Web App Launch
        Given I Launch chrome browser
        When I Open Qa Recruitment task app    

    Scenario: Badge with counter elements
        And I navigate to the header element
        * Click on the add to cart icon
        Then badge with the counter of elements in the cart should appear

    Scenario: Display counter badge only when there are items 
        And I navigate to the header element
        * move to the add to cart icon
        * No items have been added 
        Then the counter badge sh' not be displayed

    Scenario: Open Cart dropdown
        And I scroll to product list tab
        * hover over the product image
        * Add to cart bar is displayed
        When I click on the add to cart bar
        Then cart dropdown should open with listed items

    Scenario: Dropdown visibility
        And I navigate to the header element
        * click on the add to cart icon
        Then dropdown should be visible with items or empty

    Scenario: Clear Button on items
        And I navigate to the header element
        * click on the add to cart icon
        * dropdown has items listed
        * click on the clear Button
        Then All items should be removed form the cart

    Scenario: Add same Product Twice
        And I scroll to product list tab
        * hover over the product image
        * Add to cart bar is displayed
        When I click on the add to cart bar for the same product
        Then the product should be counted and added to cart as a second quantity of the same product


        


