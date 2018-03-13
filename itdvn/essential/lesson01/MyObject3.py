class MyObject:
    def __init__(self):
        self.__private_attribute = 42

    def get_attribute(self):
        return self.__private_attribute

    def set_attribute(self, value):
        if value < 100:
            self.__private_attribute = value


obj = MyObject()
print(obj.get_attribute())

obj.set_attribute(800)
print(obj.get_attribute())

obj.set_attribute(90)
print(obj.get_attribute())

obj.set_attribute(100)
print(obj.get_attribute())
