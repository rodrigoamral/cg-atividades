import math

class vec4:
    def __init__ (self, x=0, y=0, z=0, w=0):
        """
        Classe que representa um vetor de 4 dimensões.

        Args:
            x (float): Valor da coordenada x do vetor. Padrão é 0.
            y (float): Valor da coordenada y do vetor. Padrão é 0.
            z (float): Valor da coordenada z do vetor. Padrão é 0.
            w (float): Valor da coordenada w do vetor. Padrão é 0.
        """
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    #sobrecarga do operador unario -
    def __neg__(self):
        """
        Sobrecarga do operador unário - para inverter o sinal do vetor.

        Returns:
            vec4: Novo vetor com as coordenadas negativas.
        """
        return vec4(-self.x, -self.y, -self.z, -self.w)
    
    #sobrecarga do operador []
    def __getitem__ (self, i):
        """
        Sobrecarga do operador [] para acessar as coordenadas do vetor.

        Args:
            i (int): Índice da coordenada a ser acessada. Deve ser um valor entre 0 e 3.

        Returns:
            float: Valor da coordenada correspondente ao índice.
        
        Raises:
            IndexError: Se o índice estiver fora do range de 0-3.
        """
        if i==0:
            return self.x
        elif i==1:
            return self.y
        elif i==2:
            return self.z
        elif i==3:
            return self.w
        else:
            raise IndexError("index fora do range de 0-3")
        
    #sobrecarga do operador +
    def __add__(self, other):
        """
        Sobrecarga do operador + para somar dois vetores.

        Args:
            other (vec4): Outro vetor a ser somado.

        Returns:
            vec4: Novo vetor com as coordenadas somadas.
        """
        return vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    
    #sobrecarga do operador -
    def __sub__(self, other):
        """
        Sobrecarga do operador - para subtrair dois vetores.

        Args:
            other (vec4): Outro vetor a ser subtraído.

        Returns:
            vec4: Novo vetor com as coordenadas subtraídas.
        """
        return vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    
    #sobrecarga do operador *
    def __mul__(self, other):
        """
        Sobrecarga do operador * para multiplicar um vetor por um escalar ou outro vetor.

        Args:
            other (int, float, vec4): Escalar ou outro vetor a ser multiplicado.

        Returns:
            vec4: Novo vetor com as coordenadas multiplicadas.
        
        Raises:
            TypeError: Se o tipo do argumento não for compatível.
        """
        if isinstance(other, (int,float)):
            return vec4(self.x * other, self.y * other, self.z * other, self.w * other)
        elif isinstance(other, vec4):
            return vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
        else:
            raise TypeError("tipo incompativel")
        
    #sobrecarga do operador /
    def __truediv__(self, other):
        """
        Sobrecarga do operador / para dividir um vetor por um escalar.

        Args:
            other (int, float): Escalar a ser dividido.

        Returns:
            vec4: Novo vetor com as coordenadas divididas.
        
        Raises:
            TypeError: Se o tipo do argumento não for compatível.
            ZeroDivisionError: Se o escalar for igual a zero.
        """
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("divisão por zero")
            return vec4(self.x / other, self.y / other, self.z / other, self.w / other)
        
        else:
            raise TypeError("tipo incompativel")
        
    #calcula o quadrado do comprimento do vetor
    def length_squared(self):
        """
        Calcula o quadrado do comprimento do vetor.

        Returns:
            float: Quadrado do comprimento do vetor.
        """
        return self.x**2 + self.y**2 + self.z**2 + self.w**2
    
    #calcula o comprimento de um vetor
    def length(self):
        """
        Calcula o comprimento do vetor.

        Returns:
            float: Comprimento do vetor.
        """
        return math.sqrt(self.length_squared())
    
    def __str__(self):
        """
        Sobrecarga do operador str para representar o vetor como uma string.

        Returns:
            str: String com as coordenadas do vetor.
        """
        return f"({self.x}, {self.y}, {self.z}, {self.w})"
    
    #calcula produto escalar de dois vetores
    def dot(u, v):
        """
        Calcula o produto escalar de dois vetores.

        Args:
            u (vec4): Primeiro vetor.
            v (vec4): Segundo vetor.

        Returns:
            float: Produto escalar dos dois vetores.
        """
        return u.x * v.x + u.y * v.y + u.z * v.z + u.w * v.w
    
    #calcula produto vetorial de dois vetores
    def cross(u, v):
        """
        Calcula o produto vetorial de dois vetores.

        Args:
            u (vec4): Primeiro vetor.
            v (vec4): Segundo vetor.

        Returns:
            vec4: Novo vetor com o produto vetorial.
        """
        return vec4(u.y*v.z - u.z*v.y, u.z*v.x - u.x*v.z, u.x*v.y - u.y*v.x, 0)
    
    #normalizar um vetor(transformar em um vetor unitário)
    def unit_vector(v):
        """
        Normaliza um vetor, transformando-o em um vetor unitário.

        Args:
            v (vec4): Vetor a ser normalizado.

        Returns:
            vec4: Novo vetor normalizado.
        
        Raises:
            ZeroDivisionError: Se o vetor tiver comprimento igual a zero.
        """
        length = v.length()
        if length == 0:
            raise ZeroDivisionError("divisão por zero")
        return vec4(v.x / length, v.y / length, v.z / length, v.w / length)
    