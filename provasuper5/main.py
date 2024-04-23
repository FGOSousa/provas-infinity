
numeros=[1,2,3,4,5,6,7,8,9,10]
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)

from functools import reduce
soma=reduce(lambda x,y: x+y, numeros)
print(soma)

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)