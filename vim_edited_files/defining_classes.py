def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n
class Fraction:
    def __init__(self,top,bottom):

        common = gcd(top, bottom)
        self.num = top//common
        self.den = bottom//common

    def show(self):
        print('{}/{}'.format(self.num,self.den))

    def __str__(self):
        return str('{}/{}'.format(self.num,self.den))

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def int_to_frac(self, target):
        frac = Fraction(target, 1)
        return frac
    def __add__(self,other_fraction):
        if isinstance(other_fraction, Fraction):
            return Fraction(self.num*other_fraction.den + self.den*other_fraction.num, self.den * other_fraction.den)
        elif isinstance(other_fraction, int):
            other_fraction = self.int_to_frac(other_fraction)
            return Fraction(self.num*other_fraction.den + self.den*other_fraction.num, self.den * other_fraction.den)
        else:
            raise RuntimeError('Invalid object type for this opperation, only fractions or integers can be added to other fractions')


    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other_fraction):
        if isinstance(other_fraction, Fraction):
            return Fraction(self.num*other_fraction.den - self.den*other_fraction.num, self.den * other_fraction.den)
        elif isinstance(other_fraction, int):
            other_fraction = self.int_to_frac(other_fraction)
            return Fraction(self.num*other_fraction.den - self.den*other_fraction.num, self.den * other_fraction.den)
        else:
            raise RuntimeError('Invalid object type for this opperation, only fractions or integers can be subtracted from other fractions')

    def __rsub__(self,other_fraction):
        return self.__sub__(other_fraction)


    def __eq__(self, other):
        if isinstance(other, int):
            other = self.int_to_frac(other)
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum <= secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum >= secondnum



    def __mul__(self, other_fraction):
        if isinstance(other_fraction, int):
            other_fraction = self.int_to_frac(other_fraction)

        newnum = self.num * other_fraction.num
        newden = self.den * other_fraction.den
        return Fraction(newnum,newden)

    def __rmul__(self, other_fraction):
        return self.__mul__(other_fraction)

    def __truediv__(self, other_fraction):
        if isinstance(other_fraction, int):
            other_fraction = self.int_to_frac(other_fraction)

        newnum = self.num * other_fraction.den
        newden = self.den * other_fraction.num
        common = gcd(newnum,newden)
        return Fraction(newnum,newden)
    def __rtruediv__(self, other_fraction):
        return self.__truediv__(other_fraction)

f1 = Fraction(2,4)
f2 = Fraction(2,4)
f3 = Fraction(1,3)
f4 = Fraction(1,4)
f5 = Fraction(2,20)
f6 = Fraction(6,24)
f7 = Fraction(-1,2)
print(20 / f1)
print(f1-f7)
print('f6 = {}'.format(f6))
print(f5+f5)
print(f2-f6)
print(f1 == f2)
print (f1/f4)
print(f1>f4)
print(f2<f4)
print(f1-f2)
print('fração f1 = {}/{}'.format(f1.get_num(), f1.get_den()))
