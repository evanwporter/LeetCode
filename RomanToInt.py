
roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def romanToInt(s: str) -> int:


    num = 0
    prev = 0

    for sym in s:
        num += roman[sym]
        if roman[sym] > prev:
            num -= 2 * prev
        prev = roman[sym]
    return num      


print(romanToInt("III"))

