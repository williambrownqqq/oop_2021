class Rational:
    def __init__(self, numerator=5, determinator=9):
        self.numerator = numerator
        self.determinator = determinator

        @property
        def numerator(self):
            return self.__numerator

        @property
        def determinator(self):
            return self.__determinator

        @numerator.setter
        def numerator(self, numerator):
            try:
                if isinstance(numerator, int):
                    self.__numerator = numerator
            except ValueError:
                print('error')

        @determinator.setter
        def determinator(self, determinator):
            try:
                if isinstance(determinator, int):
                    self.__determinator = determinator
            except ValueError:
                print('error')

        def withdraw(self):
            print(self.__numerator)
            print("_")
            print(self.__determinator)


def main():
    abc = Rational(3, 6)
    abc.withdraw()

main()