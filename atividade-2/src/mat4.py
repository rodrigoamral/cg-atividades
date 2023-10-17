import math

class mat4:
    """
    Classe que representa uma matriz 4x4 e contém métodos para operações matemáticas com matrizes.
    """

    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0, i=0, j=0, k=0 ,l=0 ,m=0, n=0, o=0, p=0):
        """
        Construtor da classe mat4.

        Parâmetros:
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p (float): elementos da matriz 4x4. Por padrão, todos os elementos são 0.
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
        self.j = j
        self.k = k
        self.l = l
        
        self.m = m
        self.n = n
        self.o = o
        self.p = p
        
    def __add__(self, other):
        """
        Sobrecarga do operador + para adição de matrizes.

        Parâmetros:
        other (mat4): outra matriz 4x4.

        Retorna:
        mat4: uma nova matriz 4x4 que é a soma das duas matrizes.
        """
        return mat4(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d, self.e + other.e, self.f + other.f, self.g + other.g, self.h + other.h, self.i + other.i, self.j + other.j, self.k + other.k, self.l + other.l, self.m + other.m, self.n + other.n, self.o + other.o, self.p + other.p)
    
    def __sub__(self, other):
        """
        Sobrecarga do operador - para subtração de matrizes.

        Parâmetros:
        other (mat4): outra matriz 4x4.

        Retorna:
        mat4: uma nova matriz 4x4 que é a diferença entre as duas matrizes.
        """
        return mat4(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d, self.e - other.e, self.f - other.f, self.g - other.g, self.h - other.h, self.i - other.i, self.j - other.j, self.k - other.k, self.l - other.l, self.m - other.m, self.n - other.n, self.o - other.o, self.p - other.p)
    
    def __mul__(self, other):
        """
        Sobrecarga do operador * para multiplicação de matrizes ou de um escalar por uma matriz.

        Parâmetros:
        other (mat4 ou float): outra matriz 4x4 ou um escalar.

        Retorna:
        mat4: uma nova matriz 4x4 que é o resultado da multiplicação entre as duas matrizes ou entre a matriz e o escalar.
        """
        if isinstance(other, (int, float)):
            return mat4(self.a * other, self.b * other, self.c * other, self.d * other, self.e * other, self.f * other, self.g * other, self.h * other, self.i * other, self.j * other, self.k * other, self.l * other, self.m * other, self.n * other, self.o * other, self.p * other)
        
        elif isinstance(other, mat4):
            result = mat4()
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        result.elements[i][j] += self.elements[i][k] * other.elements[k][j]
            return result
        
        else:
            raise TypeError("tipo incompativel")
        
    def __str__(self):
        """
        Representação em string da matriz.

        Retorna:
        str: uma string que representa a matriz.
        """
        return f"[{self.a}, {self.b}, {self.c}, {self.d}]\n[{self.e}, {self.f}, {self.g}, {self.h}]\n[{self.i}, {self.j}, {self.k}, {self.l}]\n[{self.m}, {self.n}, {self.o}, {self.p}]"
    
    def determinant(self):
        """
        Calcula o determinante da matriz.

        Retorna:
        float: o determinante da matriz.
        """
        a, b, c, d = self.elements[0]
        e, f, g, h = self.elements[1]
        i, j, k, l = self.elements[2]
        m, n, o, p = self.elements[3]

        det = (
            a * (f * (k * p - l * o) - g * (j * p - l * n) + h * (j * o - k * n)) -
            b * (e * (k * p - l * o) - g * (i * p - l * m) + h * (i * o - k * m)) +
            c * (e * (j * p - l * n) - f * (i * p - l * m) + h * (i * n - j * m)) -
            d * (e * (j * o - k * n) - f * (i * o - k * m) + g * (i * n - j * m))
        )

        return det
    
    def inverse(self):
        """
        Calcula a inversa da matriz.

        Retorna:
        mat4: a matriz inversa.
        """
        det = self.det()

        if det == 0:
            raise ValueError("Matrix is singular, and its inverse does not exist")

        inv_det = 1 / det

        result = mat4()

        for i in range(4):
            for j in range(4):
                submatrix = [
                    [self.elements[m][n] for n in range(4) if n != j] for m in range(4) if m != i
                ]
                cofactor = submatrix.determinant()  # Chame o método determinant da submatriz
                result.elements[j][i] = cofactor * inv_det

        return result
            