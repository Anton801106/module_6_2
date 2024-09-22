# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."

class Vehicle:
    __COLOR_VARIANTS = ['red', 'yellow', 'green', 'black']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):
        return f' Модель: {self.__model}'

    def get_horsepower(self):
        return f' Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f' Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f' Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f' Нельзя сменить цвет на {self.new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fed', 'Toyota Mark II', 'RAD', '500')
vehicle1.print_info()

# Меняем свойства
print()
vehicle1.set_color('PINK')
print()
vehicle1.set_color('black')
vehicle1.owner = 'Vas'
# Проверяем
vehicle1.print_info()
