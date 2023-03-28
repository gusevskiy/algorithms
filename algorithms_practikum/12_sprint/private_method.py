
class Mainclass:
    __private_variable = 2020

    def __private_method(self):
        print("Это приватный метод")

    def insideclass(self):
        print("Приватная переменная:", Mainclass.__private_variable)
foo = Mainclass()
foo.insideclass()
foo.__private_method()