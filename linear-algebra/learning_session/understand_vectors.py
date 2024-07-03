from typing import List

# representando um vetor de floats
Vector = List[float]

# representando um vetor com o altura, peso e idade
height_weight_age = [
    70, # polegadas
    170, # libras
    40 # anos
]

# representando um vetor com as notas de provas
provas = [
    95, # prova 1
    80, # prova 2
    75, # prova 3
    62, # prova 4
]

# somas entre vetores:
# v1 + v2 = v1[0] + v2[0], v1[1] + v2[1] ..
# os vetores precisam ter o mesmo tamanho, isso é uma regra.

# Vamos tentar com listas?
#print(height_weight_age + provas)

# resultado = [70, 170, 40, 95, 80, 75, 62]
# não foi o esperado, na verdade a operação de soma entre listas, apenas junta todos os elementos em uma única lista.
# vamos constuir uma ferramenta para realizar a operação entre vetores.

def add(v: Vector, w: Vector) -> Vector:
    """
    Soma os elementos correspondentes entre dois vetores
    """

    # testando se os vetores tem o mesmo comprimento
    assert len(v) == len(w), "vetores precisam ter o mesmo tamanho"

    return [v_i + w_i for v_i, w_i in zip(v,w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

sum_vectors = add([1, 2, 3], [4, 5, 6])

#print(sum_vectors)

# subtração de vetores
def substract(v: Vector, w: Vector) -> Vector:
    """
    Subtrai os elementos correspondentes entre dois vetores
    """

    # testando se os vetores tem o mesmo comprimento
    assert len(v) == len(w), "vetores precisam ter o mesmo tamanho"

    return [v_i - w_i for v_i, w_i in zip(v,w)]

assert substract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

# operações com vários vetores
def vector_sum(vectors: List[Vector]) -> Vector:
    """
    Soma todos os elementos correspondentes entre os vetores
    """

    # verifica que os vetores não estão vazios
    assert vectors, "Não tem vetores na lista"

    # verifica se os vetores são do mesmo tamanho
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Vetores de tamanhos diferentes"
    
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

# multiplicação por escalar
def scalar_multiply(c: float, v: Vector) -> Vector:
    """
    Multiplica cada elemento do vetor por um escalar (c)
    """
    return [c * i for i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

# fazendo a média entre os elementos de cada vetores
def vector_mean(vectors: List[Vector]) -> Vector:

    n = len(vectors)
    print(n)
    print(1/n)
    return scalar_multiply(1/n, vector_sum(vectors))

v = [[1,2], [3,4], [5,6]]

v_mean = vector_mean(v)
print(v_mean)

# produto escalar -> é a soma do produto entre cada elemento de um vetor
# v1_1 * v2_1 + v1_2 * v2_2 .. + v1_n * v2_n
def dot(v: Vector, w: Vector) -> float:
    """
    Retorna a soma do produto entre cada elemento correspondente entre dois vetores
    """
    assert len(v) == len(w), "Vetores de tamanho diferentes"

    return sum(x * y for x, y in zip(v, w))

assert dot([1,2,3], [4,5,6]) == 32

#soma dos quadrados de um vetor
def sum_of_squares(v: Vector) -> float:
    """
    Retorna a soma entre os quadrados de cada elemento do vetor
    """
    assert v, "o vetor está vazio"

    return dot(v, v)

assert sum_of_squares([1,2,3]) == 14