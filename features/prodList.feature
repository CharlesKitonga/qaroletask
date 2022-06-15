Feature: Product List
  Background: Web App Launch
    Given I Launch chrome browser
    When I Open Qa Recruitment task app
    And Scroll to product list tab

  Scenario: Verify 6 Products to be displayed 
    Then Six products should be displayed

  Scenario: Display Add to Cart on Hover
    When You hover over the image
    Then Add to Cart bar should be displayed
  
  Scenario: Verify Best Seller flag can be hovered
    When You hover over the image with best seller flag
    Then One should be able to hover over Best Seller flag

  Scenario: Check Price for a Product
    When I check the price Currency for all listed products
    Then All products should have a price to them 
  
  Scenario: Price Currency
    When I check the price Currency for all listed products
    Then the Currency should be similar for all products

  Scenario: Check Product Images
    Then All products listed should have an image

  
  

