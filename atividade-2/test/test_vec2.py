import pytest
from src.vec2 import vec2

def test_constructor():
    """
    Testa o construtor da classe vec2.
    """
    v = vec2(1, 2)
    assert v.x == 1
    assert v.y == 2

def test_add():
    """
    Testa a operação de adição entre dois vetores da classe vec2.
    """
    v1 = vec2(1, 2)
    v2 = vec2(3, 4)
    result = v1 + v2
    assert result.x == 4
    assert result.y == 6
    
def test_sub():
    """
    Testa a operação de subtração entre dois vetores da classe vec2.
    """
    v1 = vec2(1, 2)
    v2 = vec2(3, 4)
    result = v1 - v2
    assert result.x == -2
    assert result.y == -2
    
def test_neg():
    """
    Testa a operação de negação unária em um vetor da classe vec2.
    """
    v = vec2(1, 2)
    result = -v
    assert result.x == -1
    assert result.y == -2

def test_get():
    """
    Testa o acesso aos elementos de um vetor da classe vec2 através do operador [].
    """
    v = vec2(1, 2)
    assert v[0] == 1
    assert v[1] == 2
    with pytest.raises(IndexError):
        v[2]
        
def test_mul():
    """
    Testa a operação de multiplicação entre um vetor da classe vec2 e um escalar.
    """
    v = vec2(1, 2)
    result = v * 2
    assert result.x == 2
    assert result.y == 4

def test_mul_vec():
    """
    Testa a operação de multiplicação entre dois vetores da classe vec2.
    """
    v1 = vec2(1, 2)
    v2 = vec2(3, 4)
    result = v1 * v2
    assert result.x == 3
    assert result.y == 8
    
def test_truediv():
    """
    Testa a operação de divisão entre um vetor da classe vec2 e um escalar.
    """
    v = vec2(1, 2)
    result = v / 2
    assert result.x == 0.5
    assert result.y == 1

def test_length_squared():
    """
    Testa o cálculo do quadrado do comprimento de um vetor da classe vec2.
    """
    v = vec2(1, 2)
    assert v.length_squared() == 5
    
def test_length():
    """
    Testa o cálculo do comprimento de um vetor da classe vec2.
    """
    v = vec2(1, 2)
    assert v.length() == pytest.approx(2.2360679775)

def test_str():
    """
    Testa a representação em string de um vetor da classe vec2.
    """
    v = vec2(1, 2)
    assert str(v) == "(1, 2)"
    
def test_dot():
    """
    Testa o cálculo do produto escalar entre dois vetores da classe vec2.
    """
    v1 = vec2(1, 2)
    v2 = vec2(3, 4)
    assert vec2.dot(v1, v2) == 11
    
def test_cross():
    """
    Testa o cálculo do produto vetorial entre dois vetores da classe vec2.
    """
    v1 = vec2(1, 2)
    v2 = vec2(3, 4)
    assert vec2.cross(v1, v2) == -2
    
def test_unit_vector():
    """
    Testa a normalização de um vetor da classe vec2.
    """
    v = vec2(1, 2)
    result = vec2.unit_vector(v)
    assert result.x == pytest.approx(0.4472135955)
    assert result.y == pytest.approx(0.894427191)





