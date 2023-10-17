from src.mat4 import mat4

def test_constructor():
    """
    Testa o construtor da classe mat4.
    """
    m = mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16)
    assert m.a == 1
    assert m.b == 2
    assert m.c == 3
    assert m.d == 4
    assert m.e == 5
    assert m.f == 6
    assert m.g == 7
    assert m.h == 8
    assert m.i == 9
    assert m.j == 10
    assert m.k == 11
    assert m.l == 12
    assert m.m == 13
    assert m.n == 14
    assert m.o == 15
    assert m.p == 16
    
def test_add():
    """
    Testa a operação de adição entre duas matrizes da classe mat4.
    """
    m1 = mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13, 14, 15, 16)
    m2 = mat4(17, 18, 19, 20, 21, 22, 23, 24, 25, 26 ,27 ,28 ,29, 30, 31, 32)
    result = m1 + m2
    assert result.a == 18
    assert result.b == 20
    assert result.c == 22
    assert result.d == 24
    assert result.e == 26
    assert result.f == 28
    assert result.g == 30
    assert result.h == 32
    assert result.i == 34
    assert result.j == 36
    assert result.k == 38
    assert result.l == 40
    assert result.m == 42
    assert result.n == 44
    assert result.o == 46
    assert result.p == 48
    
def test_sub():
    """
    Testa a operação de subtração entre duas matrizes da classe mat4.
    """
    m1 = mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13, 14, 15, 16)
    m2 = mat4(17, 18, 19, 20, 21, 22, 23, 24, 25, 26 ,27 ,28 ,29, 30, 31, 32)
    result = m1 - m2
    assert result.a == -16
    assert result.b == -16
    assert result.c == -16
    assert result.d == -16
    assert result.e == -16
    assert result.f == -16
    assert result.g == -16
    assert result.h == -16
    assert result.i == -16
    assert result.j == -16
    assert result.k == -16
    assert result.l == -16
    assert result.m == -16
    assert result.n == -16
    assert result.o == -16
    assert result.p == -16
    
def test_mul_scalar():
    """
    Testa a operação de multiplicação de uma matriz da classe mat4 por um escalar.
    """
    m = mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13, 14, 15, 16)
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
    assert result.j == 20
    assert result.k == 22
    assert result.l == 24
    assert result.m == 26
    assert result.n == 28
    assert result.o == 30
    assert result.p == 32
    
def test_mul_mat():
    """
    Testa a operação de multiplicação entre duas matrizes da classe mat4.
    """
    m1 = mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13, 14, 15, 16)
    m2 = mat4(17, 18, 19, 20, 21, 22, 23, 24, 25, 26 ,27 ,28 ,29, 30, 31, 32)
    result = m1 * m2
    assert result.a == 250
    assert result.b == 260
    assert result.c == 270
    assert result.d == 280
    assert result.e == 618
    assert result.f == 644
    assert result.g == 670
    assert result.h == 696
    assert result.i == 986
    assert result.j == 1028
    assert result.k == 1070
    assert result.l == 1112
    assert result.m == 1354
    assert result.n == 1412
    assert result.o == 1470
    assert result.p == 1528
    
def test_mul_incompatible():
    """
    Testa a operação de multiplicação de uma matriz da classe mat4 por um tipo incompatível.
    """
    m = mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13, 14, 15, 16)
    try:
        result = m * "a"
    except TypeError:
        assert True
    else:
        assert False
        
def test_str():
    """
    Testa a representação em string de uma matriz da classe mat4.
    """
    m = mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13, 14, 15, 16)
    assert str(m) == "[1, 2, 3, 4]\n[5, 6, 7, 8]\n[9, 10, 11, 12]\n[13, 14, 15, 16]"
    
def test_det():
    """
    Testa o cálculo do determinante de uma matriz da classe mat4.
    """
    m = mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13, 14, 15, 16)
    assert m.determinant() == 0
    
def test_inverse():
    """
    Testa o cálculo da inversa de uma matriz da classe mat4.
    """
    m = mat4(1, 2, 3, 0, 1, 4, 0, 0, 1, 0 ,0 ,0 ,0, 0, 0, 1)
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
    assert result.j == 0
    assert result.k == 0
    assert result.l == 0
    assert result.m == 0
    assert result.n == 0
    assert result.o == 0
    assert result.p == 1
