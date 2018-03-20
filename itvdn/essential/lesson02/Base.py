class Base:
    def method(self):
        print("Hello!")


class Child(Base):
    # pass
    def __init__(self):
        pass

    def child_method(self):
        print("Hello from child method!")

    def method(self):
        print("Hello from redefined method!")


obj = Child()
obj.method()
obj.child_method()
