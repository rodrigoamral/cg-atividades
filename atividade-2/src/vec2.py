import math

class vec2:
    """
    Classe que representa um vetor bidimensional.
    """
    
    def __init__ (self, x=0, y=0):
        """
        Construtor da classe vec2.
        
        Args:
            x (float): coordenada x do vetor.
            y (float): coordenada y do vetor.
        """
        self.x = x
        self.y = y
        
    def __neg__(self):
        """
        Sobrecarga do operador unário -.
        
        Returns:
            vec2: vetor com as coordenadas negativas.
        """
        return vec2(-self.x, -self.y)
    
    def __getitem__ (self, i):
        """
        Sobrecarga do operador [].
        
        Args:
            i (int): índice do elemento a ser acessado.
            
        Returns:
            float: valor da coordenada correspondente ao índice.
            
        Raises:
            IndexError: se o índice estiver fora do range de 0-1.
        """
        if i==0:
            return self.x
        elif i==1:
            return self.y
        else:
            raise IndexError("index fora do range de 0-1")
        
    def __add__(self, other):
        """
        Sobrecarga do operador +.
        
        Args:
            other (vec2): vetor a ser somado.
            
        Returns:
            vec2: vetor resultante da soma.
        """
        return vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """
        Sobrecarga do operador -.
        
        Args:
            other (vec2): vetor a ser subtraído.
            
        Returns:
            vec2: vetor resultante da subtração.
        """
        return vec2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        """
        Sobrecarga do operador *.
        
        Args:
            other (int, float, vec2): valor ou vetor a ser multiplicado.
            
        Returns:
            vec2: vetor resultante da multiplicação.
            
        Raises:
            TypeError: se o tipo do argumento for incompatível.
        """
        if isinstance(other, (int,float)):
            return vec2(self.x * other, self.y * other)
        elif isinstance(other, vec2):
            return vec2(self.x * other.x, self.y * other.y)
        else:
            raise TypeError("tipo incompativel")
        
    def __truediv__(self, other):
        """
        Sobrecarga do operador /.
        
        Args:
            other (int, float): valor a ser dividido.
            
        Returns:
            vec2: vetor resultante da divisão.
            
        Raises:
            TypeError: se o tipo do argumento for incompatível.
            ZeroDivisionError: se o valor do argumento for zero.
        """
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("divisão por zero")
            return vec2(self.x / other, self.y / other)
        
        else:
            raise TypeError("tipo incompativel")
        
    def length_squared(self):
        """
        Calcula o quadrado do comprimento do vetor.
        
        Returns:
            float: quadrado do comprimento do vetor.
        """
        return self.x**2 + self.y**2
    
    def length(self):
        """
        Calcula o comprimento do vetor.
        
        Returns:
            float: comprimento do vetor.
        """
        return math.sqrt(self.length_squared())
    
    def __str__(self):
        """
        Sobrecarga do operador str().
        
        Returns:
            str: representação em string do vetor.
        """
        return f"({self.x}, {self.y})"
    
    @staticmethod
    def dot(u, v):
        """
        Calcula o produto escalar de dois vetores.
        
        Args:
            u (vec2): primeiro vetor.
            v (vec2): segundo vetor.
            
        Returns:
            float: produto escalar dos vetores.
        """
        return u.x*v.x + u.y*v.y
    
    @staticmethod
    def cross(u, v):
        """
        Calcula o produto vetorial de dois vetores.
        
        Args:
            u (vec2): primeiro vetor.
            v (vec2): segundo vetor.
            
        Returns:
            float: produto vetorial dos vetores.
        """
        return u.x*v.y - u.y*v.x
    
    @staticmethod
    def unit_vector(v):
        """
        Normaliza um vetor.
        
        Args:
            v (vec2): vetor a ser normalizado.
            
        Returns:
            vec2: vetor normalizado.
            
        Raises:
            ZeroDivisionError: se o comprimento do vetor for zero.
        """
        length = v.length()
        if length == 0:
            raise ZeroDivisionError("divisão por zero")
        return vec2(v.x/length, v.y/length)
 
    