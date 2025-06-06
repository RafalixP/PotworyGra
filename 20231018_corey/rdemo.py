import requests

#r = requests.get('https://xkcd.com/353/')
r = requests.get('https://imgs.xkcd.com/comics/python.png')

print(r.status_code)
print(r.ok)
print(r.headers)

#print(r)
#print(r.text)
#print(r.content)
'''
with open('comic.png', 'wb') as f:
    f.write(r.content)
    '''