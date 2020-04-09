import re

def printRes(mo):
    if mo == None:
        print("None")
    else: 
        print(mo.group())

isPhoneNumberRegEx = re.compile(r"\(\d\d\d\)-(\d\d\d-\d\d\d\d)")
mo = isPhoneNumberRegEx.search("his is my number (905)-993-9939")

carRegex = re.compile("Car(maker|paint)"); 
mo = carRegex.search("Carmaker is here")

batRegex = re.compile(r"Bat(wo)?man")
mo = batRegex.search("Batman adventures")

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneRegex.search("My phone number is 233-9864")

supermanReg = re.compile(r"Super(wo)*man")
mo = supermanReg.search("Superwowowowowowowoman")

spidermanReg = re.compile(r"Spider(wo)+man")
mo = supermanReg.search("Spiderman")

haRegex = re.compile(r"(Ha){3}")
mo = haRegex.search("HaHaHa")

digReg = re.compile(r"(\d){3,5}?")
mo = digReg.search("A number is 322, another is 4, and another 5. R is not")

phoneRegex2 = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneRegex2.findall("090-009-0099 090-000-0090")

lyrics = "12 people, 11 animals, 10 buildings, 11 planets"
numWord = re.compile(r"\d+\s\w+")
mo = numWord.findall(lyrics)

ownClass = re.compile(r"[^aeiouAEIOU]")
mo = ownClass.findall("aklsdhjkaajfhlakjdfhklasdjfklsdjhflskdjh")

startHello = re.compile(r"^Hello")
mo = startHello.search("Hello there")

endHello = re.compile(r"Hello$")
mo = endHello.search("Hello there Hello")

allText = re.compile(r"^\d+$")
mo = allText.search("48987987")

atRegex = re.compile(r".at")
mo = atRegex.search("The cat is in the hat")

nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = nameRegex.findall("First Name: David Last Name: Lapadula")

nongreedy = re.compile(r"<(.*?)>")
mo = nongreedy.findall("<To serve humans> for dinner>")

caseIns = re.compile(r"[aeiou]", re.IGNORECASE)
mo = caseIns.findall("aklsdhjkaajfhlakjdAEIfhkSOulasdjfklsdjhflskdjh")

namesRegex = re.compile(r"Agent \w+")
mo = namesRegex.findall("Agent Alice gave us a document to Agent Robert")

namesRegex = re.compile(r"Agent (\w)\w*")
mo = namesRegex.sub(r"Agent \1****", "Agent Alice gave us a document to Agent Robert")

phoneVerbose = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d", re.VERBOSE)


