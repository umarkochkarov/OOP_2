class Products:
    def __init__(self, first=0.0, second=0.0):
        if first > second:
            raise ValueError("Illegal values of the range")

        self.__first = float(first)
        self.__second = float(second)

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, value):
        if value > self.__second:
            raise ValueError("Illegal value for the left boundary")
        self.__first = float(value)

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        if value < self.__first:
            raise ValueError("Illegal value for the right boundary")
        self.__second = float(value)

    def rangecheck(self, number):
        return self.__first <= number <= self.__second

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(float, line.split(" ", maxsplit=1)))

        first = parts[0]
        second = parts[1]

        if first > second:
            raise ValueError("Illegal values of the range")

        self.__first, self.__second = first, second

    def __str__(self):
        return f"({self.__first}, {self.__second})"

    def __imul__(self, rhs):
        if isinstance(rhs, Products):
            self.__first *= rhs.first
            self.__second *= rhs.second
            return self
        else:
            raise ValueError("Illegal type of the argument")

    def __mul__(self, rhs):
        return self.__clone().__imul__(rhs)

    def __clone(self):
        return Products(self.__first, self.__second)


if __name__ == "__main__":
    r1 = Products()
    r1.read("Введите левую и правую границы диапазона (через пробел): ")

    try:
        number_to_check = float(input("Введите число для проверки: "))
        if r1.rangecheck(number_to_check):
            print(f"{number_to_check} принадлежит диапазону {r1}")
        else:
            print(f"{number_to_check} не принадлежит диапазону {r1}")
    except ValueError:
        print("Введите корректное число для проверки.")
