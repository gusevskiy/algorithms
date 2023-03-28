def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        """Представление в дробнов виде "1/2" """
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        """Сложение"""
        newnum = (
                self.num * otherfraction.den +
                self.den * otherfraction.num
        )
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, other):
        newnum = (
                self.num * other.den -
                self.den * other.num
        )
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, other):
        """Умножение"""
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self, other):
        """Деление"""
        # деление дроби это умножение перевернув одну дробь
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum


if __name__ == '__main__':
    #  https://calcus.ru/kalkulyator-drobej
    x = Fraction(1, 2)
    y = Fraction(2, 3)
    print('1) дробь', x)
    print('2) дробь', y)
    print('+', x + y)
    print('-', x - y)
    print('*', x * y)
    print('/', x / y)
    print(x == y)
