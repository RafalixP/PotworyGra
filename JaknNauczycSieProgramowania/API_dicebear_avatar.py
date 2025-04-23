import requests
import random

from pathlib import Path

response = requests.get(f'https://api.dicebear.com/7.x/avataaars-neutral/svg')

Path ('./avatars').mkdir(exist_ok=True)

with open('./avatars/avatar.svg', 'wb') as file:
    file.write(response.content)

print(random.random())