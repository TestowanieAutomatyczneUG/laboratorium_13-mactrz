Feature: Pangram check test

  Scenario Outline: Pangram with a pangram
     Given Instance of Pangram
      When Check initiated with <input>
      Then Check will return <value>
    Examples:
    |input|value|
    |abcdefghijklmnopqrstuvwxyz|1|
    |abcdefghijklmfsafwfqnopqrstuvwxadsdyz|1|
    |abfasfas33432cdefghijk643534#$@lmnopqr$@#stuvwxyz|1|

  Scenario Outline: Pangram with not a pangram
     Given Instance of Pangram
      When Check initiated with <input>
      Then Check will return <value>
    Examples:
    |input|value|
    |abcdefghijkyz|0|
    |1421423|0|
    |(*^%(*&(|0|
    