import math

class mat2:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    #sobrecarga do operador +
    def __add__(self, other):
        return mat2(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
    
    #sobrecarga do operador -
    def __sub__(self, other):
        return mat2(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d)
    
    #sobrecarga do operador * para multiplicação por escalar ou outra matriz
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return mat2(self.a * other, self.b * other, self.c * other, self.d * other)
        elif isinstance(other, mat2):
            return mat2(
                self.a * other.a + self.b * other.c,
                self.a * other.b + self.b * other.d,
                self.c * other.a + self.d * other.c,
                self.c * other.b + self.d * other.d
            )
        else:
            raise TypeError("tipo incompativel")
        
    #representação em string da matriz
    def __str__(self):
        return f"[{self.a}, {self.b}]\n[{self.c}, {self.d}]"
    
    #calcular o determinante de uma matriz
    def det(self):
        return self.a * self.d - self.b * self.c
    
    #calcular a inversa de uma matriz
    def inverse(self):
        det = self.det()
        if det == 0:
            raise ZeroDivisionError("matriz não inversivel")
        return mat2(self.d, -self.b, -self.c, self.a) * (1/det)