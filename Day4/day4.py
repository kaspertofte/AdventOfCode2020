# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def byrValidator(value):
    if(len(value) != 4):
        return False
    try:
        iValue = int(value)
        if(iValue < 1920 or 2002 < iValue):
            return False
    except:
        return False
    return True

# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def iyrValidator(value):
    if(len(value) != 4):
        return False
    try:
        iValue = int(value)
        if(iValue < 2010 or 2020 < iValue):
            return False
    except:
        return False
    return True

# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def eyrValidator(value):
    if(len(value) != 4):
        return False
    try:
        iValue = int(value)
        if(iValue < 2020 or 2030 < iValue):
            return False
    except:
        return False
    return True

# hgt (Height) - a number followed by either cm or in:
  # If cm, the number must be at least 150 and at most 193.
  # If in, the number must be at least 59 and at most 76.
def hgtValidator(value):
    unit = value[len(value)-2:len(value)]
    val = 0
    try:
        val = int(value[0:len(value)-2])
    except:
        return False
    if(unit == "cm"):
        return 150 <= val and val <= 193
    elif unit=="in":
        return 59 <= val and val <= 76
    else:
        return False

#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
numRange=range(48,58)
charRange=range(97,103)
validOrd = set(numRange).union(set(charRange))
def hclValidator(value):
    if(len(value) != 7):
        return False

    if(value[0] != "#"):
        return False
    for c in value[1:len(value)]:
        if not (ord(c) in validOrd):
            return False
    return True

# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
validEcl = [
  "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
]
def eclValidator(value):
    return value in validEcl

# pid (Passport ID) - a nine-digit number, including leading zeroes.
def pidValidator(value):
    if(len(value) != 9):
        return False
    try:
        val = int(value)
    except:
        return False
    return True

validators = {
    "byr":byrValidator,
    "iyr":iyrValidator,
    "eyr":eyrValidator,
    "hgt":hgtValidator,
    "hcl":hclValidator,
    "ecl":eclValidator,
    "pid":pidValidator,
    }
optionalFields=["cid"]

def numValidPassports(filepath):
    with open(filepath, "r") as file:
        data = file.read().strip().split("\n\n")

    result = 0
    for passport in data:
        fields = passport.split()
        numRequiredFields = 0
        for field in fields:
            entry=field.split(":")
            if((entry[0] in validators.keys()) and (validators[entry[0]](entry[1]))):
                numRequiredFields = numRequiredFields + 1
        if(numRequiredFields == len(validators)):
            result = result + 1
    return result
