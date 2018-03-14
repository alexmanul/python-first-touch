class Complex:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return "Complex({!r), {!r})".format(self.real, self.imaginary)

    def __str__(self):
        return "{}{:+d}i".format(self.real, self.imaginary)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real, self.imaginary * other.imaginary)

    def __neg__(self):
        return Complex(-self.real, -self.imaginary)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary


c = Complex(2, 5)
print(c)

print(Complex(5, -3))
print(Complex(2, 3) - Complex(1, 1))

print(abs(8))
print(abs(Complex(2, 3)))