class Person:
    def print_info(self):
        print(self.name, "is", self.age)


john = Person()
john.name = "John"
john.age = 22

lucy = Person()
lucy.name = "Lucy"
lucy.age = 21

print(john.name, "is", john.age)
print(lucy.name, "is", lucy.age)

Person.print_info(john)
Person.print_info(lucy)

john.print_info()
lucy.print_info()
