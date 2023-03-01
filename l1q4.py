#faça um programa que peça as 4 notas bimestrais e mostre a media
#somar as 4 notas dividir por 4
#entrada das notas
nota1 = float(input('Digite a primeira nota: '
,))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

#calculo da media
media = (nota1 + nota2 + nota3 + nota4) /4

#exibir o resultado
print('a media das {} {} {} {} notas é {:,2f}',
format (nota1, nota3, nota4, media))