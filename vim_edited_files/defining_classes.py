def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n
class Fraction:
    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom

    def show(self):
        print('{}/{}'.format(self.num,self.den))

    def __str__(self):
        return str('{}/{}'.format(self.num,self.den))


    def __add__(self,other_fraction):
        newnum = self.num*other_fraction.den + self.den*other_fraction.num
        newden = self.den * other_fraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum

    def __sub__(self, other_fraction):
        newnum = self.num*other_fraction.den - self.den*other_fraction.num
        newden = self.den * other_fraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)


    def __mul__(self, other_fraction):

        newnum = self.num * other_fraction.num
        newden = self.den * other_fraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __truediv__(self, other_fraction):

        newnum = self.num * other_fraction.den
        newden = self.den * other_fraction.num
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

f1 = Fraction(2,4)
f2 = Fraction(2,4)
f3 = Fraction(1,3)
f4 = Fraction(1,4)
print(f1 == f2)
print (f1/f4)
print(f1>f4)
print(f2<f4)
print(f1-f2)
