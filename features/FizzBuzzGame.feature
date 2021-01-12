Feature: Fizzbuzz test

  Scenario: Game of Fizzbuzz with number 15
     Given Instance of Fizzbuzz
      When Game initiated with 15
      Then Game will return FizzBuzz

  Scenario: Game of Fizzbuzz with number 3
     Given Instance of Fizzbuzz
      When Game initiated with 3
      Then Game will return Fizz

  Scenario: Game of Fizzbuzz with number 5
     Given Instance of Fizzbuzz
      When Game initiated with 5
      Then Game will return Buzz

  Scenario Outline: Game of Fizzbuzz with a number divisible by 3
     Given Instance of Fizzbuzz
      When Game initiated with <number>
      Then Game will return <result>
    Examples:
      |number |result|
      |3      |Fizz|
      |6      |Fizz|

  Scenario Outline: Game of Fizzbuzz with a number divisible by 5 or 15
     Given Instance of Fizzbuzz
      When Game initiated with <number>
      Then Game will return <result>
    Examples:
      |number |result|
      |20      |Buzz|
      |30      |FizzBuzz|