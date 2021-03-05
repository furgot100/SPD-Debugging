class Person:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email
    
    def send_hiring_email(self):
        print("email sent to: ", self.email())

first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
    ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

person1 = Person(
    'Elizabeth',
    'Debicki',
    1990,
    ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],
    'deb@makeschool.com'
)

person2 = Person(
    'Jim',
    'Carrey',
    1962,
    ['Ace Ventura', 'The Mask', 'Dumb and Dumber', 'The Truman Show', 'Yes Man'],
    'jim@makeschool.com'
)

people = [person1, person2]
    
for person in people:
    if person.birth_year > 1985:
        print(person.first_name, person.last_name)
        print('Movies Played: ', end='')
        for m in person.movies:
            print(m, end=', ')
        print()
        person.send_hiring_email()