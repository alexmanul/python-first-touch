class MyObject:
    def __init__(self):
        self.__private_attribute = 42

    def get_private(self):
        return self.__private_attribute


obj = MyObject()
obj.get_private()

# obj.__private_attribute - error!

print(obj.get_private())
print(obj._MyObject__private_attribute)
