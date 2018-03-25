def check_instance(obj, cls):
    return cls in type(obj).mro()


def check_subclass(child, base):
    return base in child.mro()


if __name__ == '__main__':
    print(check_instance(8, int))
    print(check_instance(8, str))
    print(check_instance(True, int))
    print(check_instance("asdf", object))

    print()

    print(check_subclass(bool, int))
    print(check_subclass(bool, object))
    print(check_subclass(bool, str))

    print()

    print(issubclass(int, int))
    print(check_subclass(bool, bool))
