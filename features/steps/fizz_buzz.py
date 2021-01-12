from behave import *
from src.FizzBuzz import FizzBuzz

@given("Instance of Fizzbuzz")
def step_impl(context):
    context.product = FizzBuzz()

@when("Game initiated with 15")
def step_impl(context):
    context.result = str(context.product.game(15))

@then("Game will return FizzBuzz")
def step_impl(context):
    assert "FizzBuzz" == context.result

@when("Game initiated with 3")
def step_impl(context):
    context.result = str(context.product.game(3))

@then("Game will return Fizz")
def step_impl(context):
    assert "Fizz" == context.result

@when("Game initiated with 5")
def step_impl(context):
    context.result = str(context.product.game(5))

@then("Game will return Buzz")
def step_impl(context):
    assert "Buzz" == context.result

@when("Game initiated with {number}")
def step_impl(context, number):
    context.result = str(context.product.game(int(number)))

@then("Game will return {result}")
def step_impl(context, result):
    assert result == context.result