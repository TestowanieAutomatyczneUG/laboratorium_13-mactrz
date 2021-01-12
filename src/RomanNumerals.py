import math

class Roman:
    def roman(self, number):
        napis = ""
        baseROM = ""
        base = 1
        while number != 0:
            if number >= 1000:
                base = 1000
                baseROM = "M"
            elif number >= 900:
                base = 900
                baseROM = "CM"
            elif number >= 500:
                base = 500
                baseROM = "D"
            elif number >= 400:
                base = 400
                baseROM = "CD"
            elif number >= 100:
                base = 100
                baseROM = "C"
            elif number >= 90:
                base = 90
                baseROM = "XC"
            elif number >= 50:
                base = 50
                baseROM = "L"
            elif number >= 40:
                base = 40
                baseROM = "XL"
            elif number >= 10:
                base = 10
                baseROM = "X"
            elif number >= 9:
                base = 9
                baseROM = "IX"
            elif number >= 5:
                base = 5
                baseROM = "V"
            elif number >= 4:
                base = 4
                baseROM = "IV"
            elif number >= 1:
                base = 1
                baseROM = "I"

            howmany = number // base
            number = number - (howmany*base)
            napis += howmany * baseROM
        return napis