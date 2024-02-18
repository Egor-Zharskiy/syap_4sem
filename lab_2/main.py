import sys
from datetime import datetime


def search_persons_by_age(persons):
    min_age = int(input('Введите минимальную дату для поиска: '))
    max_age = int(input('Введите максимальную дату для поиска: '))

    result = []
    for person in persons:
        age = person.calculate_age()
        if min_age <= age <= max_age:
            result.append(person)
    return result


class Person:
    def __init__(self, surname, birth_date, faculty):
        self.surname = surname
        self.birth_date = birth_date
        self.faculty = faculty

    def __setattr__(self, key, value):
        if key == 'birth_date':
            try:
                datetime.strptime(value, '%d-%m-%Y')
            except ValueError:
                print("неверный формат ввода даты. Допустимый формат: д-м-г")
                sys.exit()

        super().__setattr__(key, value)

    def __str__(self):
        return (f'\nФамилия: {self.surname};'
                f'\nДата рождения: {self.birth_date};'
                f'\nФакультет: {self.faculty};'
                f'\nВозраст: {self.calculate_age()};')

    def calculate_age(self):
        birth_date = datetime.strptime(self.birth_date, '%d-%m-%Y')
        today = datetime.today()
        age = today.year - birth_date.year
        return age


class Abiturient(Person):
    def __init__(self, surname, birth_date, faculty):
        super().__init__(surname, birth_date, faculty)

    def __str__(self):
        return (f'{super().__str__()}'
                f'\nФакультет: {self.faculty};')


class Student(Person):
    def __init__(self, surname, birth_date, faculty, course):
        super().__init__(surname, birth_date, faculty)
        self.course = course

    def __str__(self):
        return (f'{super().__str__()}'
                f'\nФакультет: {self.faculty};'
                f'\nКурс: {self.course}')


class Teacher(Person):
    def __init__(self, surname, birth_date, faculty, position, experience):
        super().__init__(surname, birth_date, faculty)
        self.position = position
        self.experience = experience

    def __str__(self):
        return (f'{super().__str__()}'
                f'\nДолжность: {self.position};'
                f'\nОпыт: {self.experience}')


person_list = [
    Person('Шамрило', '01-01-1990', 'ФКП'),
    Abiturient('Воронов', '15-05-2000', 'ФИТУ'),
    Student('Марецкий', '10-08-1998', 'ИЭФ', 3),
    Teacher('Войтович', '05-03-1985', 'ФКСИС', 'Профессор', 10),
]

print(*[person.surname for person in search_persons_by_age(person_list)])
