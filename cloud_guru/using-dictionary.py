# 1) Set the emails variable to be an empty dict

emails = {}
assert emails == {}, f"Expected 'emails' to be {{}} but got: {repr(emails)}"

# 2) Add ashley to the emailsdict  without reassigning the variable

emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
assert emails == {"ashley": "ashley@example.com",
                  "craig":"craig@example.com"}, f"Expected 'emails' to be {{'ashley': 'ashley@example.com', 'craig':'craig@example.com'}} but got: {repr(emails)}"

#del emails["craig"]

#assert emails == {"ashley": "ashley@example.com"}, f"Expected 'emails' to be {{'ashley': 'ashley@example.com'}} but got: {repr(emails)}"
print(emails)

users = list(emails.keys())

print(users)

users = list(emails.values())

print(users)

pairs = list(emails.items())
print(pairs)
print(ord('a'))
print(ord('\u2122'))
print(chr(8382))
print(chr(8482))