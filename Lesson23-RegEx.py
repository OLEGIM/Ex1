import re

mytext = "kolya, 1922, 33, dasha, kolya78@corp.com"" \
""slava, 927, 24, masha, slava45@corp.com"" \
""Vasya, 26, 21, olya, vasya23@corp.com"" \
""petya, 35, 31, anna petya12@corp.com"


"""
\d = AnyDigit
\D = Any not Digit
\w = Any Alphabet Symbol
\W = Any not Alphabet Symbol
\s = BreakSpace
\s = Not BreakSpace


[0-9]{3}
[A-Z][a-z]+
@\w+\.\w -search domain

"""

textlokkfor = r"@\w+\.\w+"
allresults = re.findall(textlokkfor, mytext)

print(allresults)
