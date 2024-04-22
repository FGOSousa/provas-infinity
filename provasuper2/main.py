par=[]
impar=[]

for i in range(10):
    numero=int(input("Digite um número aleatório: "))
    if numero%2==0:
        par.append(numero)
    else:
        impar.append(numero)


print(f'Números pares: ',(par))
print(f'Números impares: ',(impar))
print(f'Tamanho da lista: ',(len(par) + len(impar)))

number = 0
lista_completa = par + impar

for i in (lista_completa):
    number += i

print(f'Soma dos itens da lista: ', (number))