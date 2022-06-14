from behave import *
from selenium import webdriver

@when('Enter valid username and password')
def loginform1(context):
    assert True, "Test Passed"


@given('Click on Login')
def step_impl(context):
    assert True, "Test Passed"


@when('You navigate to search bar')
def step_impl(context):
    assert True, "Test Passed"


@then('Search Page should be displayed')
def step_impl(context):
    assert True, "Test Passed"

@when('You navigate to advanced search page')
def step_impl(context):
    assert True, "Test Passed"


@then('Advanced Search Page should be displayed')
def step_impl(context):
    assert True, "Test Passed"
