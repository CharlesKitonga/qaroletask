Feature: Product List
  Background: Web App Launch
    Given I Launch chrome browser
    When I Open Qa Recruitment task app

Scenario: Featured Product Artwork
    And I scroll through above product list section
    Then I should find a product flagged as a featured artwork 
    
        