#! python3

import re, pyperclip

phonNumReg = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
\d{3}
(\s|-|\.)
\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?
)''', re.VERBOSE)

emailReg = re.compile(r'''
[a-zA-z0-9_.+]+
@
[a-zA-z0-9_.+]+
''', re.VERBOSE)

text = pyperclip.paste()

phoneNumbers = phonNumReg.findall(text)
emails = emailReg.findall(text)

allPhoneNumbers = []
for phoneNumber in phoneNumbers: 
    allPhoneNumbers.append(phoneNumber[0])

resultPhones = ",\n".join(allPhoneNumbers)
resultEmails = ",\n".join(emails)
results = resultPhones + "\n\n" + resultEmails

pyperclip.copy(results)

