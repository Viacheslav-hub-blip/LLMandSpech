class Cat():
    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age

    def meow(self):
        print('мяу')

    def purr(self):
        print('мррр')


def summa(a, b):
    return a * b


print(summa('a', 3))
