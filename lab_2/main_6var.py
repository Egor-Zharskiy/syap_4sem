import sys


class Car:
    def __init__(self, color, type, year):
        self.__color = color
        self.__type = type
        self.__year = year
        self.__is_started = False

    def start_engine(self):
        if not self.__is_started:
            print('Сначала заведите автомобиль!')
        else:
            self.__is_started = True
            print('Автомобиль заведен')

    def stop_engine(self):
        if self.__is_started:
            self.__is_started = False
            print('Автомобиль заглушен')
        else:
            print("Автомобиль уже заглушен")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, car_year):
        if not isinstance(car_year, int):
            raise Exception("Неверный тип данных")
        else:
            self.__year = car_year

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, car_type):
        self.__type = car_type

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, car_color):
        self.__color = car_color

    @staticmethod
    def input_car_data():
        color = input('Введите цвет автомобиля: ')
        car_type = input('Введите тип автомобиля: ')
        year = input('Введите год выпуска автомобиля: ')

        try:
            year = int(year)
        except ValueError:
            print('Неверный формат года. Год должен быть целым числом.')
            sys.exit()

        return Car(color, car_type, year)

    def __str__(self):
        return (f"Цвет автомобиля: {self.color}"
                f"\nТип автомобиля: {self.type}"
                f"\nГод выпуска автомобиля: {self.year}")


if __name__ == '__main__':
    car = Car.input_car_data()
    print(car)
