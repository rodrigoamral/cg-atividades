import math

class vec4:
    def __init__ (self, x=0, y=0, z=0, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    #sobrecarga do operador unario -
    def __neg__(self):
        return vec4(-self.x, -self.y, -self.z, -self.w)
    
    #sobrecarga do operador []
    def __get__ (self, i):
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
        return vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    
    #sobrecarga do operador -
    def __sub__(self, other):
        return vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    
    #sobrecarga do operador *
    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return vec4(self.x * other, self.y * other, self.z * other, self.w * other)
        elif isinstance(other, vec4):
            return vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
        else:
            raise TypeError("tipo incompativel")
        
    #sobrecarga do operador /
    def __trudiv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("divisão por zero")
            return vec4(self.x / other, self.y / other, self.z / other, self.w / other)
        
        else:
            raise TypeError("tipo incompativel")
        
    #calcula o quadrado do comprimento do vetor
    def length_squared(self):
        return self.x**2 + self.y**2 + self.z**2 + self.w**2
    
    #calcula o comprimento de um vetor
    def length(self):
        return math.sqrt(self.length_squared())
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z}, {self.w})"
    
    #calcula produto escalar de dois vetores
    def dot(u, v):
        return u.x * v.x + u.y * v.y + u.z * v.z + u.w * v.w
    
    #calcula produto vetorial de dois vetores
    def cross(u, v):
        return vec4(u.y*v.z - u.z*v.y, u.z*v.x - u.x*v.z, u.x*v.y - u.y*v.x, 0)
    
    #normalizar um vetor(transformar em um vetor unitário)
    def unit_vector(v):
        length = v.length()
        if length == 0:
            raise ZeroDivisionError("divisão por zero")
        return vec4(v.x / length, v.y / length, v.z / length, v.w / length)
    