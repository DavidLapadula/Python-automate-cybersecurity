import pprint
message = 'It was a bright cold day in April, and we are in quarantine'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)