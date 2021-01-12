from behave import *
from src.Pangram import Pangram

@given("Instance of Pangram")
def step_impl(context):
    context.product = Pangram()

@when("Check initiated with {input}")
def step_impl(context, input):
    context.result = context.product.check(input)

@then("Check will return {value}")
def step_impl(context, value):
    assert bool(int(value)) == context.result