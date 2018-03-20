class Base(object):
    def method(self):
        print("Method class: ", type(self).__name__)
        print("Instance class: ", type(self).__name__)


class Child(Base):
    pass


def main():
    base_instance = Base()
    child_instance = Child()

    base_instance.method()
    child_instance.method()


if __name__ == '__main__':
    main()
