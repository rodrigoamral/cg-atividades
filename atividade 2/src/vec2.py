import math

class vec4:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y
        
    #sobrecarga do operador unario -
    def __neg__(self):
        return vec4(-self.x, -self.y)
    
    #sobrecarga do operador []
    def __get__ (self, i):
        if i==0:
            return self.x
        elif i==1:
            return self.y
        else:
            raise IndexError("index fora do range de 0-1")
        
    #sobrecarga do operador +
    def __add__(self, other):
        return vec4(self.x + other.x, self.y + other.y)
    
    #sobrecarga do operador -
    def __sub__(self, other):
        return vec4(self.x - other.x, self.y - other.y)
    
    #sobrecarga do operador *
    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return vec4(self.x * other, self.y * other)
        elif isinstance(other, vec4):
            return vec4(self.x * other.x, self.y * other.y)
        else:
            raise TypeError("tipo incompativel")
        
    #sobrecarga do operador /
    def __trudiv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("divisão por zero")
            return vec4(self.x / other, self.y / other)
        
        else:
            raise TypeError("tipo incompativel")
        
    #calcula o quadrado do comprimento do vetor
    def length_squared(self):
        return self.x**2 + self.y**2
    
    #calcula o comprimento de um vetor
    def length(self):
        return math.sqrt(self.length_squared())
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    #calcular o produto escalar de dois vetores
    def dot(u, v):
        return u.x*v.x + u.y*v.y
    
    #calcular o produto vetorial de dois vetores
    def cross(u, v):
        return u.x*v.y - u.y*v.x
    
    #normalizar um vetor
    def unit_vector(v):
        length = v.length()
        if length == 0:
            raise ZeroDivisionError("divisão por zero")
        return vec4(v.x/length, v.y/length)
    
    