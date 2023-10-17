from src.mat3 import mat3

def test_constructor():
    """
    Testa o construtor da classe mat3.
    """
    m = mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert m.a == 1
    assert m.b == 2
    assert m.c == 3
    assert m.d == 4
    assert m.e == 5
    assert m.f == 6
    assert m.g == 7
    assert m.h == 8
    assert m.i == 9
    
def test_add():
    """
    Testa a operação de adição entre duas matrizes.
    """
    m1 = mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
    m2 = mat3(10, 11, 12, 13, 14, 15, 16, 17, 18)
    result = m1 + m2
    assert result.a == 11
    assert result.b == 13
    assert result.c == 15
    assert result.d == 17
    assert result.e == 19
    assert result.f == 21
    assert result.g == 23
    assert result.h == 25
    assert result.i == 27
    
def test_sub():
    """
    Testa a operação de subtração entre duas matrizes.
    """
    m1 = mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
    m2 = mat3(10, 11, 12, 13, 14, 15, 16, 17, 18)
    result = m1 - m2
    assert result.a == -9
    assert result.b == -9
    assert result.c == -9
    assert result.d == -9
    assert result.e == -9
    assert result.f == -9
    assert result.g == -9
    assert result.h == -9
    assert result.i == -9
    
def test_mul_scalar():
    """
    Testa a operação de multiplicação de uma matriz por um escalar.
    """
    m = mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
    result = m * 2
    assert result.a == 2
    assert result.b == 4
    assert result.c == 6
    assert result.d == 8
    assert result.e == 10
    assert result.f == 12
    assert result.g == 14
    assert result.h == 16
    assert result.i == 18
    
def test_mul_mat():
    """
    Testa a operação de multiplicação entre duas matrizes.
    """
    m1 = mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
    m2 = mat3(10, 11, 12, 13, 14, 15, 16, 17, 18)
    result = m1 * m2
    assert result.a == 84
    assert result.b == 90
    assert result.c == 96
    assert result.d == 201
    assert result.e == 216
    assert result.f == 231
    assert result.g == 318
    assert result.h == 342
    assert result.i == 366
    
def test_mul_incompatible():
    """
    Testa a operação de multiplicação de uma matriz por um tipo incompatível.
    """
    m = mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
    try:
        result = m * "a"
    except TypeError:
        assert True
    else:
        assert False
        
def test_str():
    """
    Testa a representação em string de uma matriz.
    """
    m = mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert str(m) == "[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]"
    
def test_det():
    """
    Testa o cálculo do determinante de uma matriz.
    """
    m = mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert m.det() == 0
    
def test_inverse():
    """
    Testa o cálculo da inversa de uma matriz.
    """
    m = mat3(1, 2, 3, 0, 1, 4, 0, 0, 1)
    result = m.inverse()
    assert result.a == 1
    assert result.b == -2
    assert result.c == 5
    assert result.d == 0
    assert result.e == 1
    assert result.f == -4
    assert result.g == 0
    assert result.h == 0
    assert result.i == 1
    
    