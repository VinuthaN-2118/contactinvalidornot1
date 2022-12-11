import re
def isvalid(s):
    Pattern = re.compile("(0|91)?[6-9] [0-9] {9}")
    return Pattern.match(s)
s = "2124567"
if (isvalid(s)):
    print("valid number")
else:
    print("Invalid number")
