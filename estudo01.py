nota1 = nota2 = 0.0
media = 0.0

nota1 =float(input('Digite a primeira nota: '))
nota2 =float(input('Digite a segunda nota '))
media = (nota1+ nota2)/ 2
if (media >= 7):
    print('resultado aprovado')
    print('parabens')
elif (media>=5):
    print('voce esta de recuperação')
else:
    print('resultado negado')
    print('tente novamente.')

print('sua média é {}'.format(media))
