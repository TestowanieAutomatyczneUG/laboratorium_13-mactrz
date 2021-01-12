Feature: RomanNumerals test

  Scenario Outline: Roman numeral given <number>
     Given Instance of Roman
      When roman initiated with <number>
      Then roman will return <result>
    Examples:
    |number|result|
    |2     |II    |
    |3     |III   |
    |11    |XI    |
    |25    |XXV   |
    |139   |CXXXIX|
    |240   |CCXL  |
    |570   |DLXX  |
    |1449  |MCDXLIX|
