from src.mat2 import mat2

def test_constructor():
    """
    Testa o construtor da classe mat2.
    """
    m = mat2(1, 2, 3, 4)
    assert m.a == 1
    assert m.b == 2
    assert m.c == 3
    assert m.d == 4
    
def test_add():
    """
    Testa a operação de adição entre duas matrizes da classe mat2.
    """
    m1 = mat2(1, 2, 3, 4)
    m2 = mat2(5, 6, 7, 8)
    result = m1 + m2
    assert result.a == 6
    assert result.b == 8
    assert result.c == 10
    assert result.d == 12
    
def test_sub():
    """
    Testa a operação de subtração entre duas matrizes da classe mat2.
    """
    m1 = mat2(1, 2, 3, 4)
    m2 = mat2(5, 6, 7, 8)
    result = m1 - m2
    assert result.a == -4
    assert result.b == -4
    assert result.c == -4
    assert result.d == -4

def test_mul_scalar():
    """
    Testa a operação de multiplicação por escalar entre uma matriz da classe mat2 e um número.
    """
    m = mat2(1, 2, 3, 4)
    result = m * 2
    assert result.a == 2
    assert result.b == 4
    assert result.c == 6
    assert result.d == 8

def test_mul_mat():
    """
    Testa a operação de multiplicação entre duas matrizes da classe mat2.
    """
    m1 = mat2(1, 2, 3, 4)
    m2 = mat2(5, 6, 7, 8)
    result = m1 * m2
    assert result.a == 19
    assert result.b == 22
    assert result.c == 43
    assert result.d == 50
    
def test_mul_incompatible():
    """
    Testa a operação de multiplicação entre uma matriz da classe mat2 e um tipo incompatível.
    """
    m = mat2(1, 2, 3, 4)
    try:
        result = m * "a"
    except TypeError:
        assert True
    else:
        assert False
        
def test_str():
    """
    Testa a representação em string de uma matriz da classe mat2.
    """
    m = mat2(1, 2, 3, 4)
    assert str(m) == "[1, 2]\n[3, 4]"

def test_det():
    """
    Testa o cálculo do determinante de uma matriz da classe mat2.
    """
    m = mat2(1, 2, 3, 4)
    assert m.det() == -2
    
def test_inverse():
    """
    Testa o cálculo da inversa de uma matriz da classe mat2.
    """
    m = mat2(1, 2, 3, 4)
    result = m.inverse()
    assert result.a == -2
    assert result.b == 1
    assert result.c == 1.5
    assert result.d == -0.5
    
def gerar_documentacao():
    """
    Gera a documentação da classe mat2 em português-br.
    """
    # código para gerar a documentação em português-br
