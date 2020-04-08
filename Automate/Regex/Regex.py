import re

# No regex
def isPhoneNumber(text): 
    if len(text) != 12: 
        return False
    for i in range(0, 3):
        if not text[i].isdecimal(): 
                return False
    if text[3] != "-":
        return False;
    for i in range(4, 7):
        if not text[i].isdecimal(): 
                return False
    if text[7] != "-":
        return False;
    for i in range(8, 12):
        if not text[i].isdecimal(): 
                return False
    return True

isntNum = "982347289374928374"
isNum = "905-993-9939"
hasNum = "This is my number (905)-993-9939"

isPhoneNumberRegEx = re.compile(r"\(\d\d\d\)-(\d\d\d-\d\d\d\d)")
match = isPhoneNumberRegEx.search(hasNum)
match.group()

carRegex = re.compile("Car(maker|paint)"); 
mo = carRegex.search("Carmaker is here")
print(mo.group())