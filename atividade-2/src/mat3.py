import math

class mat3:
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0, i=0):
        """
        Classe que representa uma matriz 3x3.

        Args:
            a (float): valor da posição (1,1) da matriz. Default é 0.
            b (float): valor da posição (1,2) da matriz. Default é 0.
            c (float): valor da posição (1,3) da matriz. Default é 0.
            d (float): valor da posição (2,1) da matriz. Default é 0.
            e (float): valor da posição (2,2) da matriz. Default é 0.
            f (float): valor da posição (2,3) da matriz. Default é 0.
            g (float): valor da posição (3,1) da matriz. Default é 0.
            h (float): valor da posição (3,2) da matriz. Default é 0.
            i (float): valor da posição (3,3) da matriz. Default é 0.
        """
        self.a = a
        self.b = b
        self.c = c
        
        self.d = d
        self.e = e
        self.f = f
        
        self.g = g
        self.h = h
        self.i = i
    
    def __add__(self, other):
        """
        Sobrecarga do operador + para somar duas matrizes.

        Args:
            other (mat3): outra matriz 3x3.

        Returns:
            mat3: matriz resultante da soma.
        """
        return mat3(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d, self.e + other.e, self.f + other.f, self.g + other.g, self.h + other.h, self.i + other.i)
    
    def __sub__(self, other):
        """
        Sobrecarga do operador - para subtrair duas matrizes.

        Args:
            other (mat3): outra matriz 3x3.

        Returns:
            mat3: matriz resultante da subtração.
        """
        return mat3(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d, self.e - other.e, self.f - other.f, self.g - other.g, self.h - other.h, self.i - other.i)
    
    def __mul__(self, other):
        """
        Sobrecarga do operador * para multiplicação por escalar ou outra matriz.

        Args:
            other (int, float, mat3): escalar ou outra matriz 3x3.

        Returns:
            mat3: matriz resultante da multiplicação.
        
        Raises:
            TypeError: se o tipo de other não for compatível.
        """
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
        
    def __str__(self):
        """
        Representação em string da matriz.

        Returns:
            str: string que representa a matriz.
        """
        return f"[{self.a}, {self.b}, {self.c}]\n[{self.d}, {self.e}, {self.f}]\n[{self.g}, {self.h}, {self.i}]"
    
    def det(self):
        """
        Calcula o determinante da matriz.

        Returns:
            float: determinante da matriz.
        """
        return self.a * self.e * self.i + self.b * self.f * self.g + self.c * self.d * self.h - self.c * self.e * self.g - self.b * self.d * self.i - self.a * self.f * self.h
    
    def inverse(self):
        """
        Calcula a inversa da matriz.

        Returns:
            mat3: matriz inversa.

        Raises:
            ZeroDivisionError: se a matriz não for inversível.
        """
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
    