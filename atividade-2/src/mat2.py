import math

class mat2:
    """
    Classe que representa uma matriz 2x2.
    """
    
    def __init__(self, a=0, b=0, c=0, d=0):
        """
        Construtor da classe mat2.

        Args:
            a (float): valor da posição (1,1) da matriz (default 0).
            b (float): valor da posição (1,2) da matriz (default 0).
            c (float): valor da posição (2,1) da matriz (default 0).
            d (float): valor da posição (2,2) da matriz (default 0).
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def __add__(self, other):
        """
        Sobrecarga do operador + para somar duas matrizes.

        Args:
            other (mat2): outra matriz a ser somada.

        Returns:
            mat2: resultado da soma das duas matrizes.
        """
        return mat2(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
    
    def __sub__(self, other):
        """
        Sobrecarga do operador - para subtrair duas matrizes.

        Args:
            other (mat2): outra matriz a ser subtraída.

        Returns:
            mat2: resultado da subtração das duas matrizes.
        """
        return mat2(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d)
    
    def __mul__(self, other):
        """
        Sobrecarga do operador * para multiplicação por escalar ou outra matriz.

        Args:
            other (int, float, mat2): valor escalar ou outra matriz a ser multiplicada.

        Returns:
            mat2: resultado da multiplicação da matriz por um escalar ou outra matriz.
        
        Raises:
            TypeError: se o tipo de other não for compatível.
        """
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
        
    def __str__(self):
        """
        Representação em string da matriz.

        Returns:
            str: representação em string da matriz.
        """
        return f"[{self.a}, {self.b}]\n[{self.c}, {self.d}]"
    
    def det(self):
        """
        Calcula o determinante da matriz.

        Returns:
            float: determinante da matriz.
        """
        return self.a * self.d - self.b * self.c
    
    def inverse(self):
        """
        Calcula a inversa da matriz.

        Returns:
            mat2: inversa da matriz.

        Raises:
            ZeroDivisionError: se a matriz não for inversível.
        """
        det = self.det()
        if det == 0:
            raise ZeroDivisionError("matriz não inversivel")
        return mat2(self.d, -self.b, -self.c, self.a) * (1/det)
