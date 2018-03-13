class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, "is", self.age)


jack = Person("Jack", 50)
anna = Person("Anna", 25)

jack.print_info()
anna.print_info()
