class Mammoth:
    __count = 0

    def __new__(cls, *args, **kwargs):
        if Mammoth.__count < 3:
            instance = super().__new__(cls)
            cls.__count += 1
            print('Создан мамонт')
            return instance
        print('Мамонты вымерли')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'{self.name}  {self.age} left {3 - Mammoth.__count}')


small_mammoth = Mammoth('Lenny', 54)
small_mammoth.show_info()
small_mammoth = Mammoth('Vlad', 54)
small_mammoth.show_info()
