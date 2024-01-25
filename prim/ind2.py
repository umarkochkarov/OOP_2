class Rational:
    MAX_SIZE = 100  # Максимальный размер списка

    def __init__(self, numerator_size, denominator_size):
        if numerator_size > self.MAX_SIZE or denominator_size > self.MAX_SIZE:
            raise ValueError("Размер числителя или знаменателя превышает максимально допустимый размер")

        self.numerator = [0] * self.MAX_SIZE
        self.denominator = [0] * self.MAX_SIZE
        self.size_numerator = numerator_size
        self.size_denominator = denominator_size

    def size(self):
        return max(self.size_numerator, self.size_denominator)

    def __getitem__(self, index):
        if index < 0 or index >= self.MAX_SIZE:
            raise IndexError("Индекс выходит за пределы допустимого диапазона")

        return (self.numerator[index], self.denominator[index])

    def __setitem__(self, index, value):
        if index < 0 or index >= self.MAX_SIZE:
            raise IndexError("Индекс выходит за пределы допустимого диапазона")

        numerator, denominator = value
        self.numerator[index] = numerator
        self.denominator[index] = denominator

# Пример использования класса
rational_number = Rational(numerator_size=5, denominator_size=5)
rational_number[0] = (3, 4)
rational_number[1] = (1, 2)

print("Размер:", rational_number.size())
print("Элемент с индексом 0:", rational_number[0])
print("Элемент с индексом 1:", rational_number[1])
