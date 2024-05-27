class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # ЖК "такой-то": этаж / всего этажей
        print(f'----- ЖК "{self.name}": этаж {new_floor}/{self.number_of_floors}')
        # Печатать этажи, если в диапазоне, иначе — сообщение об ошибке
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor+1):
                print(f'Этаж {i}')
        else:
            if new_floor <= 0:
                # Отрицательное число в скобках
                print(f'({new_floor}) — Такого этажа не существует')
            else:
                # Положительное число
                print(f'{new_floor} — Такого этажа не существует')


h1 = House('Панорама', 25)
h2 = House('Любимово', 28)
h1.go_to(7)
h2.go_to(-5)
h2.go_to(35)

