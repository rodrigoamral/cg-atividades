import math

class vec3:
    def __init__ (self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    #sobrecarga do operador unario -
    def __neg__(self):
        return vec3(-self.x, -self.y, -self.z)
    
    #sobrecarga do operador []
    def __get__ (self, i):
        if i==0:
            return self.x
        elif i==1:
            return self.y
        elif i==2:
            return self.z
        else:
            raise IndexError("index fora do range de 0-2")
        
    #sobrecarga do operador +
    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    #sobrecarga do operador -
    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    #sobrecarga do operador *
    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return vec3(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, vec3):
            return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            raise TypeError("tipo incompativel")
        
    #sobrecarga do operador /    
    def __trudiv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("divisão por zero")
            return vec3(self.x / other, self.y / other, self.z / other)
        
        else:
            raise TypeError("tipo incompativel")
        
    #calcula o quadrado do comprimento do vetor    
    def length_squared(self):
        return self.x**2 + self.y**2 + self.z**2
    
    #calcula o comprimento de um vetor
    def length(self):
        return math.sqrt(self.length_squared())
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    #calcular produto escalar de dois vetores
    def dot(u, v):
        return u.x * v.x + u.y * v.y + u.z * v.z
    
    #calcular o produto vetorial de dois vetores
    def cross(u, v):
        return vec3(u.y * v.z - u.z * v.y, u.z * v.x - u.x * v.z, u.x * v.y - u.y * v.x)
    
    #normalizar um vetor(transformar em um vetor unitário)
    def unit_vector(v):
        length = v.length()
        if length == 0:
            raise ZeroDivisionError("Não é possivel normalizar um vetor de comprimento 0")
        return vec3(v.x / length, v.y / length, v.z / length)

        
    
    
            