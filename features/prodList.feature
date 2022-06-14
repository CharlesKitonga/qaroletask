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
