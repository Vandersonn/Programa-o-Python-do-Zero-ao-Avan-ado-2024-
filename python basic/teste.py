
name = input('Qual é o seu nome ')
idade = str(input('qual é sua idade '))
cidade = input('Onde vocẽ mora ')
# simplificando o if

idade = int(idade)
print('não elegivel' if idade < 18 else 'Elegivel')

print(f'Okay {name}, vocẽ tem {idade} anos '
      f'e mora em {cidade}.')



