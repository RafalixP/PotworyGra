'''
1. Make a sublist with anime parameters
2. Use the input function (mood, runtime, series/movie)'''

# create list of animes
animes = [
    ['naruto', 'pepehype', 'forever', 'series'],
    ['haikyuu', 'sports', 'short', 'series'],
    ['mushishi', 'chill', 'short', 'series'],
    ['march comes in like a lion', 'slice of life', 'short', 'series']
]
# input mood, desirable lenght and type movie/series
print('_'*10)
print('Witaj w ułatwiaczu wyborów. Zajmiemy się wybraniem odpowiedniego anime dla Ciebie.')
mood  = input('Powiedz, czyli napisz w jakim nastroju obecnie jesteś pepehype/sports/chill/slice of life: ')
length = input('Powiedz jak długi film chciałbyś obejrzeć forever/short: ')
type = input('Powiedz czy chciałbyś oglądać serial czy tylko pojedyńczy film series/movie: ')

print(f'Hej, dzięki za podanie informacji. Rozpoczynam szukanie utworów pasujących do {mood} nastroju, o długości mniej więcej {length} i ograniczę się do {type}')

#loop through and find matching mood

for anime in animes:
    if anime[1] == mood:
        print(f'Dla Twojego obecnego nastroju czyli {mood} proponuję obejrzeć {anime[0]} anime.')

print('Przyjemnego oglądania')
print('_'*10)