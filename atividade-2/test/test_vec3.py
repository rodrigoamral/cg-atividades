import pytest
from src.vec3 import vec3

def test_constructor():
    """
    Testa o construtor da classe vec3.
    """
    v = vec3(1, 2, 3)
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3
    
def test_add():
    """
    Testa a operação de adição entre dois vetores da classe vec3.
    """
    v1 = vec3(1, 2, 3)
    v2 = vec3(4, 5, 6)
    result = v1 + v2
    assert result.x == 5
    assert result.y == 7
    assert result.z == 9
    
def test_sub():
    """
    Testa a operação de subtração entre dois vetores da classe vec3.
    """
    v1 = vec3(1, 2, 3)
    v2 = vec3(4, 5, 6)
    result = v1 - v2
    assert result.x == -3
    assert result.y == -3
    assert result.z == -3

def test_neg():
    """
    Testa a operação de negação unária de um vetor da classe vec3.
    """
    v = vec3(1, 2, 3)
    result = -v
    assert result.x == -1
    assert result.y == -2
    assert result.z == -3
    
def test_get():
    """
    Testa o acesso aos elementos de um vetor da classe vec3 através do operador [].
    """
    v = vec3(1, 2, 3)
    assert v[0] == 1
    assert v[1] == 2
    assert v[2] == 3
    with pytest.raises(IndexError):
        v[3]

def test_mul():
    """
    Testa a operação de multiplicação de um vetor da classe vec3 por um escalar.
    """
    v = vec3(1, 2, 3)
    result = v * 2
    assert result.x == 2
    assert result.y == 4
    assert result.z == 6
    
def test_mul_vec():
    """
    Testa a operação de multiplicação entre dois vetores da classe vec3.
    """
    v1 = vec3(1, 2, 3)
    v2 = vec3(4, 5, 6)
    result = v1 * v2
    assert result.x == 4
    assert result.y == 10
    assert result.z == 18
    
def test_truediv():
    """
    Testa a operação de divisão de um vetor da classe vec3 por um escalar.
    """
    v = vec3(1, 2, 3)
    result = v / 2
    assert result.x == 0.5
    assert result.y == 1
    assert result.z == 1.5

def test_cross():
    """
    Testa a operação de produto vetorial entre dois vetores da classe vec3.
    """
    v1 = vec3(1, 2, 3)
    v2 = vec3(4, 5, 6)
    result = v1.cross(v2)
    assert result.x == -3
    assert result.y == 6
    assert result.z == -3
    
def test_dot():
    """
    Testa a operação de produto escalar entre dois vetores da classe vec3.
    """
    v1 = vec3(1, 2, 3)
    v2 = vec3(4, 5, 6)
    result = v1.dot(v2)
    assert result == 32
    
def test_unit_vector():
    """
    Testa a operação de normalização de um vetor da classe vec3.
    """
    v = vec3(1, 2, 3)
    result = v.unit_vector()
    assert result.x == pytest.approx(0.2672612419124244)
    assert result.y == pytest.approx(0.5345224838248488)
    assert result.z == pytest.approx(0.8017837257372732)
