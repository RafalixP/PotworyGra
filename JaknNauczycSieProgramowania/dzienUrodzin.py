import datetime
import calendar

while True:
    date_of_birth = input('podaj datę urodzenia w formacie dd-mm-rrrr: ')
    day, month, year  = date_of_birth.split('-')

    data_urodzenia = datetime.datetime(int(year), int(month), int(day))

    #print(data_urodzenia.weekday())

    day_name = calendar.day_name[data_urodzenia.weekday()]


    def translate_to_polish(day_name):
        match day_name:
            case 'Monday':
                return 'Poniedziałek'
            case 'Tuesday':
                return 'wtorek'
            case 'Wednesday':
                return 'środa'
            case 'Thursday':
                return 'czwartunio'
            case 'Friday':
                return 'piątunio' 
            case 'Saturday':
                return 'sobota'  
            case 'Sunday':
                return 'niedziela'  
        
    #print(day_name)

    print(translate_to_polish(day_name))


    print()

'''print(day)
print(month)
print(year)
print(date_of_birth)'''