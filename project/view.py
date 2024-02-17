from controller import ControllerCadastro, ControllerLogin

while True:
    print('SISTEMA DE CADASTRO E LOGIN\n')
    try:
        option = int(input('DIGITE (1) PARA CADASTRAR\nDIGITE (2) PARA FAZER LOGIN\n'))
    except:
        print('DIGITE APENAS NÚMEROS, NÃO É ACEITO OUTRO TIPO DE CARACTERE')
        break
    
    while option != 1 and option != 2:
        option = int(input('\nOPÇÃO INVÁLIDA\nDIGITE (1) PARA CADASTRAR\nDIGITE (2) PARA FAZER LOGIN\n'))
    
    if option == 1:
        print('\nOPÇÃO SELECIONADA: CADASTRAR')
        name = input("Nome: ")
        last_name = input("Sobrenome: ")
        birthdate = input("Data de nascimento mm/dd/aaaa: ")
        email = input("Email: ")
        password = input("Senha: ")
        NEW_REGISTER = ControllerCadastro.register(name, last_name, birthdate, email, password)

        print('')
        if NEW_REGISTER == 1:
            print('CADASTRO REALIZADO COM SUCESSO')
        elif NEW_REGISTER == 2:
            print('NOME DEVE CONTER DE 3 A 50 CARACTERES')
        elif NEW_REGISTER == 3:
            print('SOBRENOME DEVE CONTER DE 3 A 50 CARACTERES')
        elif NEW_REGISTER == 4:
            print('DATA DE DE NASCIMENTO NÃO ATENDE O PADRÃO mm/dd/aaa')
        elif NEW_REGISTER == 5:
            print('EMAIL NÃO ATENDE O PADRÃO nome@email.com')
        elif NEW_REGISTER == 6:
            print('SENHA DEVE CONTER AO MENOS 8 CARACTERES')
        elif NEW_REGISTER == 7:
            print('ENDEREÇO DE EMAIL JÁ CADASTRADO')
        elif NEW_REGISTER == 8:
            print('OUTRO ERRO')
        break

    print('\nOPÇÃO SELECIONADA: FAZER LOGIN')
    email = input('Email: ')
    password = input('Password: ')
    NEW_LOGIN = ControllerLogin.login_attempt(email, password)

    print('')
    if NEW_LOGIN == 1:
        print('LOGIN COM SUCESSO')
    elif NEW_LOGIN == 2:
        print('EMAIL NÃO REGISTRADO')
    elif NEW_LOGIN == 3:
        print('SENHA INCORRETA')
    break
