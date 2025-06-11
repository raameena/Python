"""
seperate string by characters
each char = calls key and adds to toal
add values together
"""

"""
if the sequence of *** exists in x
then that is the key

"""
mySymbols = mySymbols = {"I": 1, "V": 5, "X": 10, "L": 50, 
                         "C": 100, "D": 500, "M": 1000}

doubleSymbols = {"IV" : 4, "IX" : 9, "XL" : 40,
                "XC" : 90, "CD" : 400, "CM" : 900}

s = "MCMXCIV"
# M CM XC IV
total = 0

for a,b in zip(s,s[1:]):
    chars = a + b
    if chars in doubleSymbols:
        total = total + doubleSymbols[chars]
        s = s.replace(chars,"")

for char in s:
    total = total + mySymbols[char]



print(total)