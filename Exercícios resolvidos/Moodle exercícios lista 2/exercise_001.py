# Faça um programa que verifique se uma pessoa é ou não maior de idade.

print('Bem-vindo ao programa de verificação de maioridade!')

idade = int(input('Digite a idade: '))

if idade < 0:
    print('\nErro! Não existe idade negativa')
elif idade < 18:
    print('\nA pessoa NÃO é maior de idade')
else:
    print('\nA pessoa é maior de idade')
