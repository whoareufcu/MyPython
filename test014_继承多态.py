class Animal(object):
    def run(self):
        print("Animal is running")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


d = Dog()
d.run()
c = Cat()
c.run()
