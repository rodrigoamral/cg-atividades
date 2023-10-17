import math

class vec3:
    """
    Classe que representa um vetor tridimensional.
    """

    def __init__ (self, x=0, y=0, z=0):
        """
        Construtor da classe vec3.

        Args:
            x (float): Valor da coordenada x do vetor. Default é 0.
            y (float): Valor da coordenada y do vetor. Default é 0.
            z (float): Valor da coordenada z do vetor. Default é 0.
        """
        self.x = x
        self.y = y
        self.z = z

    def __neg__(self):
        """
        Sobrecarga do operador unário -.

        Returns:
            vec3: Um novo vetor com as coordenadas negativas do vetor original.
        """
        return vec3(-self.x, -self.y, -self.z)
    
    def __getitem__ (self, i):
        """
        Sobrecarga do operador [].

        Args:
            i (int): Índice do elemento desejado. Deve ser um valor entre 0 e 2.

        Returns:
            float: Valor da coordenada correspondente ao índice informado.

        Raises:
            IndexError: Se o índice informado estiver fora do range de 0 a 2.
        """
        if i==0:
            return self.x
        elif i==1:
            return self.y
        elif i==2:
            return self.z
        else:
            raise IndexError("index fora do range de 0-2")
        
    def __add__(self, other):
        """
        Sobrecarga do operador +.

        Args:
            other (vec3): Outro vetor a ser somado com o vetor original.

        Returns:
            vec3: Um novo vetor com as coordenadas resultantes da soma dos vetores originais.
        """
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        """
        Sobrecarga do operador -.

        Args:
            other (vec3): Outro vetor a ser subtraído do vetor original.

        Returns:
            vec3: Um novo vetor com as coordenadas resultantes da subtração dos vetores originais.
        """
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        """
        Sobrecarga do operador *.

        Args:
            other (int, float, vec3): Outro valor ou vetor a ser multiplicado com o vetor original.

        Returns:
            vec3: Um novo vetor com as coordenadas resultantes da multiplicação dos vetores originais ou do vetor original por um valor escalar.
        
        Raises:
            TypeError: Se o tipo do argumento informado não for compatível com a operação de multiplicação.
        """
        if isinstance(other, (int,float)):
            return vec3(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, vec3):
            return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            raise TypeError("tipo incompativel")
        
    def __truediv__(self, other):
        """
        Sobrecarga do operador /.

        Args:
            other (int, float): Valor escalar pelo qual o vetor original será dividido.

        Returns:
            vec3: Um novo vetor com as coordenadas resultantes da divisão do vetor original pelo valor escalar.

        Raises:
            TypeError: Se o tipo do argumento informado não for compatível com a operação de divisão.
            ZeroDivisionError: Se o valor escalar informado for igual a zero.
        """
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("divisão por zero")
            return vec3(self.x / other, self.y / other, self.z / other)
        
        else:
            raise TypeError("tipo incompativel")
        
    def length_squared(self):
        """
        Calcula o quadrado do comprimento do vetor.

        Returns:
            float: O quadrado do comprimento do vetor.
        """
        return self.x**2 + self.y**2 + self.z**2
    
    def length(self):
        """
        Calcula o comprimento do vetor.

        Returns:
            float: O comprimento do vetor.
        """
        return math.sqrt(self.length_squared())
    
    def __str__(self):
        """
        Sobrecarga do operador str.

        Returns:
            str: Uma string representando o vetor no formato (x, y, z).
        """
        return f"({self.x}, {self.y}, {self.z})"
    
    @staticmethod
    def dot(u, v):
        """
        Calcula o produto escalar de dois vetores.

        Args:
            u (vec3): Um vetor.
            v (vec3): Outro vetor.

        Returns:
            float: O produto escalar dos vetores informados.
        """
        return u.x * v.x + u.y * v.y + u.z * v.z
    
    @staticmethod
    def cross(u, v):
        """
        Calcula o produto vetorial de dois vetores.

        Args:
            u (vec3): Um vetor.
            v (vec3): Outro vetor.

        Returns:
            vec3: Um novo vetor com as coordenadas resultantes do produto vetorial dos vetores informados.
        """
        return vec3(u.y * v.z - u.z * v.y, u.z * v.x - u.x * v.z, u.x * v.y - u.y * v.x)
    
    @staticmethod
    def unit_vector(v):
        """
        Normaliza um vetor, transformando-o em um vetor unitário.

        Args:
            v (vec3): Um vetor.

        Returns:
            vec3: Um novo vetor com as coordenadas normalizadas do vetor original.

        Raises:
            ZeroDivisionError: Se o comprimento do vetor original for igual a zero.
        """
        length = v.length()
        if length == 0:
            raise ZeroDivisionError("Não é possivel normalizar um vetor de comprimento 0")
        return vec3(v.x / length, v.y / length, v.z / length)
        
    
    
            