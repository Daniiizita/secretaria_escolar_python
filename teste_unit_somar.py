def somar(a, b):
    return a + b

# Teste unitário para a função somar
def test_somar():
    # Teste com números positivos
    assert somar(2, 3) == 5
    
    # Teste com um número positivo e um negativo
    assert somar(2, -3) == -1
    
    # Teste com números negativos
    assert somar(-2, -3) == -5

test_somar()  # Chama a função de teste
