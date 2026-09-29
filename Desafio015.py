km = int(input('Quantos km foram percorridos no carro? '))
dia = int(input('Á quantos dias ele foi alugado? '))

resultado = dia * 60 + km * 0.15

print('Quanto você deve pelo aluguel do carro: R${}'.format(resultado))
