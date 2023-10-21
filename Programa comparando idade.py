name = input("Qual é seu nome? ")
age = int(input("Quantos anos vocês tem? "))
if age == 26:
    print(f'Olá {name}, eu também tenho 26 anos, será que nascemos no mesmo mês?')
    mes = input('Em qual mês você nasceu? ')
    if mes == 'dezembro':
        prinr(f'Nossa, que coincidência, eu também sou de dezembro"')
    else:
        print(f'Que bacana que você nasceu em {mes}, eu sou um pouco mais novo que você, pois nasci em dezembro.')
else:
    print(f'Então você tem {age} anos! Isso faz com que eu seja... ')
    if age < 26:
        print(f'mais velho que você!')
    else:
        print(f'mais novo que você!')
if age != 26:
    bet = int(input(f'Tente advinhar minha idade: '))
    if bet == 26:
        print('Na mosca, eu tenho 26 anos!')
    elif bet < 26:
        while bet < 26:
            print('Um pouco mais...' )
            bet = int(input('Tente novamente: '))
            if bet == 26:
                print ('Na mosca, eu tenho 26 anos.')
    else:
        while bet > 26:
            print('Um pouco menos...')
            bet = int(input('Tente novamente: '))
        print ('Na mosca, eu tenho 26 anos!')
print (f'Foi um prazer te conhecer um pouco, {name}, adeus!')
            
