# Matrizes é uma coleção bidimensional (linhas e colunas) de números.
# Matriz[i][j] quer dizer que estamos nos referindo ao elemento na linha i e coluna j

# o tipo matriz

from typing import List

Matrix = List[List[float]]

#criando uma matriz
A = [[1,2,3], # 2 linhas e 3 colunas
     [4,5,6]]

B = [[1,2], # 3 linhas e 2 colunas
     [3,4],
     [5,6]]

print(len(A[0])) # Quantidade de colunas da matriz
print(len(A)) # Quantidade de linhas

from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    """
    Retorna a quantidade de linhas e colunas da matriz
    """

    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # se A não estiver fazia,
                                    # retorna o número de elementos da primeira lista
    
    return num_rows, num_cols

assert shape([[1,2,3], [4,5,6]]) == (2,3)