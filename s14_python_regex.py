import re

text = "The agent's phone number is 408-555-1234. Call soon!"
print('phone' in text)

pattern = 'phone'
print(re.search(pattern, text))

pattern = 'NOT IN TEXT'
print(re.search(pattern, text))

pattern = 'phone'
match = re.search(pattern, text)

print(match.span())
print(match.start())
print(match.end())

pattern = 'my phone once, my phone twice'
matches = re.findall('phone', pattern)
print(len(matches))

for match in re.finditer('phone', pattern):
    print(match.group)

print('Manual search:')
text = 'My phone number is 408-555-1234'
phone = re.search('408-555-1234', text)
print(phone)
print('RegEx search:')
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone)
print(phone.group())

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)
print(phone.group())

# Compile - make it easier to extract group values
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print(results.group())
# Indexing starts at position 1, not 0
print(results.group(1))
print(results.group(1, 2))

# or operator in regex
or_res = re.search(r'cat|dog', 'The cat is here')
print(or_res)

wild_res = re.findall(r'...at', 'The cat in the hat went splat.')
print(wild_res)

# ^ sign - starts with
wild2_res = re.findall(r'^\d', '1 is a number')
print(wild2_res)

# $ sign - ends with
wild3_res = re.findall(r'\d$', 'The number is 2')
print(wild3_res)

# exclusion with a pattern
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+'
print(re.findall(pattern, phrase))

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
clean = re.findall(r'[^!.? ]+', test_phrase)
print(' '.join(clean))

text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
pattern = r'[\w]+-[\w]+'

print(re.findall(pattern, text))

text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r'cat(fish|nap|claw)', text))
