import math

class mat3:
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0, i=0):
        self.a = a
        self.b = b
        self.c = c
        
        self.d = d
        self.e = e
        self.f = f
        
        self.g = g
        self.h = h
        self.i = i
    
    #sobrecarga do operador +
    def __add__(self, other):
        return mat3(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d, self.e + other.e, self.f + other.f, self.g + other.g, self.h + other.h, self.i + other.i)
    
    #sobrecarga do operador -
    def __sub__(self, other):
        return mat3(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d, self.e - other.e, self.f - other.f, self.g - other.g, self.h - other.h, self.i - other.i)
    
    #sobrecarga do operador * para multiplicação por escalar ou outra matriz
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return mat3(self.a * other, self.b * other, self.c * other, self.d * other, self.e * other, self.f * other, self.g * other, self.h * other, self.i * other)
        elif isinstance(other, mat3):
            return mat3(
                self.a * other.a + self.b * other.d + self.c * other.g,
                self.a * other.b + self.b * other.e + self.c * other.h,
                self.a * other.c + self.b * other.f + self.c * other.i,
                
                self.d * other.a + self.e * other.d + self.f * other.g,
                self.d * other.b + self.e * other.e + self.f * other.h,
                self.d * other.c + self.e * other.f + self.f * other.i,
                
                self.g * other.a + self.h * other.d + self.i * other.g,
                self.g * other.b + self.h * other.e + self.i * other.h,
                self.g * other.c + self.h * other.f + self.i * other.i
            )
        else:
            raise TypeError("tipo incompativel")
        
    #representação em string da matriz
    def __str__(self):
        return f"[{self.a}, {self.b}, {self.c}]\n[{self.d}, {self.e}, {self.f}]\n[{self.g}, {self.h}, {self.i}]"
    
    #calcular o determinante de uma matriz
    def det(self):
        return self.a * self.e * self.i + self.b * self.f * self.g + self.c * self.d * self.h - self.c * self.e * self.g - self.b * self.d * self.i - self.a * self.f * self.h
    
    #calcular a inversa de uma matriz
    def inverse(self):
        det = self.det()
        if det == 0:
            raise ZeroDivisionError("matriz não inversivel")
        return mat3(
            self.e * self.i - self.f * self.h,
            self.c * self.h - self.b * self.i,
            self.b * self.f - self.c * self.e,
            
            self.f * self.g - self.d * self.i,
            self.a * self.i - self.c * self.g,
            self.c * self.d - self.a * self.f,
            
            self.d * self.h - self.e * self.g,
            self.b * self.g - self.a * self.h,
            self.a * self.e - self.b * self.d
        ) * (1/det)
        
    