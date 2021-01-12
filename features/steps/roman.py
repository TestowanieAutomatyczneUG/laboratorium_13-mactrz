from behave import *
from src.RomanNumerals import Roman

@given("Instance of Roman")
def step_impl(context):
    context.roman = Roman()

@when("roman initiated with {number}")
def step_impl(context, number):
    context.result = str(context.roman.roman(int(number)))

@then("roman will return {result}")
def step_impl(context, result):
    assert result == context.result