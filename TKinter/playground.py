def add(*args):
    output=0
    for n in args:
        output+=n
    return output

print(add(1,2,3))


def calculate(n, **kwargs):
    # print(kwargs)
    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(5, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")


my_car = Car(make="Nissan")