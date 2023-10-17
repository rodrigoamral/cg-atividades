import pytest
from src.vec4 import vec4

def test_constructor():
    """
    Testa o construtor da classe vec4.
    """
    v = vec4(1, 2, 3, 4)
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3
    assert v.w == 4

def test_add():
    """
    Testa a operação de adição entre dois vetores da classe vec4.
    """
    v1 = vec4(1, 2, 3, 4)
    v2 = vec4(5, 6, 7, 8)
    result = v1 + v2
    assert result.x == 6
    assert result.y == 8
    assert result.z == 10
    assert result.w == 12
    
def test_sub():
    """
    Testa a operação de subtração entre dois vetores da classe vec4.
    """
    v1 = vec4(1, 2, 3, 4)
    v2 = vec4(5, 6, 7, 8)
    result = v1 - v2
    assert result.x == -4
    assert result.y == -4
    assert result.z == -4
    assert result.w == -4

def test_neg():
    """
    Testa o operador unário de negação da classe vec4.
    """
    v = vec4(1, 2, 3, 4)
    result = -v
    assert result.x == -1
    assert result.y == -2
    assert result.z == -3
    assert result.w == -4
    
def test_get():
    """
    Testa o operador [] da classe vec4.
    """
    v = vec4(1, 2, 3, 4)
    assert v[0] == 1
    assert v[1] == 2
    assert v[2] == 3
    assert v[3] == 4
    with pytest.raises(IndexError):
        v[4]

def test_mul():
    """
    Testa a operação de multiplicação por escalar da classe vec4.
    """
    v = vec4(1, 2, 3, 4)
    result = v * 2
    assert result.x == 2
    assert result.y == 4
    assert result.z == 6
    assert result.w == 8
    
def test_mul_vec():
    """
    Testa a operação de multiplicação entre dois vetores da classe vec4.
    """
    v1 = vec4(1, 2, 3, 4)
    v2 = vec4(5, 6, 7, 8)
    result = v1 * v2
    assert result.x == 5
    assert result.y == 12
    assert result.z == 21
    assert result.w == 32
    
def test_truediv():
    """
    Testa a operação de divisão por escalar da classe vec4.
    """
    v = vec4(1, 2, 3, 4)
    result = v / 2
    assert result.x == 0.5
    assert result.y == 1
    assert result.z == 1.5
    assert result.w == 2
    
def test_length():
    """
    Testa o cálculo do comprimento de um vetor da classe vec4.
    """
    v = vec4(1, 2, 3, 4)
    assert v.length() == 5.477225575051661
    assert v.length_squared() == 30
    
def test_length_squared():
    """
    Testa o cálculo do quadrado do comprimento de um vetor da classe vec4.
    """
    v = vec4(1, 2, 3, 4)
    assert v.length_squared() == 30
    
def test_str():
    """
    Testa a representação em string de um vetor da classe vec4.
    """
    v = vec4(1, 2, 3, 4)
    assert str(v) == "(1, 2, 3, 4)"
    
def test_cross():
    """
    Testa o cálculo do produto vetorial entre dois vetores da classe vec4.
    """
    v1 = vec4(1, 2, 3, 4)
    v2 = vec4(5, 6, 7, 8)
    result = vec4.cross(v1, v2)
    assert result.x == -4
    assert result.y == 8
    assert result.z == -4
    assert result.w == 0
    
def test_dot():
    """
    Testa o cálculo do produto escalar entre dois vetores da classe vec4.
    """
    v1 = vec4(1, 2, 3, 4)
    v2 = vec4(5, 6, 7, 8)
    result = vec4.dot(v1, v2)
    assert result == 70
    
def test_unit_vector():
    """
    Testa a normalização de um vetor da classe vec4.
    """
    v = vec4(1, 2, 3, 4)
    result = v.unit_vector()
    assert result.x == pytest.approx(0.18257418583505536)
    assert result.y == pytest.approx(0.3651483716701107)
    assert result.z == pytest.approx(0.5477225575051661)
    assert result.w == pytest.approx(0.7302967433402214)
