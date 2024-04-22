notas=[]

def media ():
    total=0
    for i in notas:
        total+=i
    media=total/len(notas)
    return media

def verifyApprove(media):
    if media == 10:
        return "parabéns"
    elif media >= 7.0:
        return "aprovado"
    else:
        return "reprovado"
for i in range(4):
    nota=float(input('Digite a nota '+str(i + 1)+': '))
    notas.append(nota)

media_total = media()
print('Média: ', (media_total))
print('O aluno foi: ', (verifyApprove(media_total)))
