# 1.Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками
# def securityCard(a):
#     a = list(str(a))
#     for i in range(12):
#         a[i] = '*'
#     print(*a)
# securityCard(1234568979777894)
# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
# def reverse(s):
#     return s[::-1]
# def palindorm(s):
#     rev = reverse(s)
#     if s == rev:
#         print(True)
#     else:
#         print(False)
# palindorm('шалаш')
# 3. Решите задачу
a=0
class tomato:
    states = {0: 'только посадили', 1: 'цветок', 2: 'еще зеленый', 3: 'созрел'}

    def __init__(self, index):
        self._states = 0
        self._index = index

    def _change_state(self):
        if self._states < 3:
            self._states += 1
        self._print_state()

    def _print_state(self):
        print(f'Томат {self._index} , {tomato.states[self._states]}')

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._states == 3:
            return True
        return False


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self, a=0):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []



class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('---------------')
        print('Садовник работает...')
        self._plant.grow_all()
        print('Готово')
        print('---------------')




    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('---------------')
            print('Урожай собран')
            print('---------------')
        else:
            print('---------------')
            print('Томаты еще не созрели')
            print('---------------')

def knowledge_base():
    print('справка по садоводству: .....')


knowledge_base()
great_tomato_bush = TomatoBush(4)
gardener = Gardener('Emilio', great_tomato_bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()

