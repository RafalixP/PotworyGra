users = []

assert users == [], f"Expected 'users' to be [] but got: {repr(users)}"

users.append('kevin')
users.append('bob')
users.append('alice')

assert users == ['kevin', 'bob', 'alice'], f"Expected 'users' to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"
#assert users == ['kevin', 'alice'], f"Expected 'users' to be ['kevin', 'alice'] but got: {repr(users)}"

del users[1]

assert users == ['kevin', 'alice'], f"Expected 'users' to be ['kevin', 'alice'] but got: {repr(users)}"

rev_users = list(reversed(users))
assert rev_users == ['alice', 'kevin'], f"Expected 'users' to be ['alice', 'kevin'] but got: {repr(users)}"

users.insert(1,"melody")
assert users == ['kevin', 'melody', 'alice'], f"Expected 'users' to be ['kevin', 'melody', 'alice'] but got: {repr(users)}"

users += ['andy', 'wanda']
assert users == ['kevin', 'melody', 'alice', 'andy', 'wanda'], f"Expected 'users' to be ['kevin', 'melody', 'alice', 'andy', 'wanda'] but got: {repr(users)}"

center_users = users[2:4]
assert center_users == ['alice', 'andy'], f"Expected 'users' to be ['alice', 'andy'] but got: {repr(users)}"

