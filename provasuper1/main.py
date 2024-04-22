
email='construcaoadm@gmail.com'
senha='cons1234'

while True:
    emailcad=input('Digite seu email: ')
    if emailcad==email:
        senhacad=input('Digite sua senha: ')
        if senhacad==senha:
            print('Acesso permitido')
            break
        else: 
            print("Senha incorreta")
    else:
        print("Email incorreto")