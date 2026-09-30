print('↓ Conversor de temperaturas ↓')

print('-------------------------------------------')

print('Escolha uma unidade de medida entre |°C|, |°F| ou |°K|')
pergunta = input('Escreva em minusculo (c, f ou k): ')

t = float(input('Agora digite a temperatura: '))

print('-------------------------------------------')

print('Deseja converter {} para |°C|, |°F| ou para |°K|?'.format(t))
pergunta2 = input('Escreva em minusculo (c, f ou k): ')

print('-------------------------------------------')

if pergunta == pergunta2:
    print('Uai, é a mesma coisa: {}'.format(t))

elif pergunta == 'c':
    if pergunta2 == 'f':
        print('Resultado da conversão: {}°C → {:.1f}°F'.format(t, (t * 1.8) + 32))
    elif pergunta2 == 'k':
        print('Resultado da conversão entre: {}°C → {:.1f}°K'.format(t ,t + 273.15))

elif pergunta == 'f':
    if pergunta2 == 'c':
        print('Resultado da conversão: {}°F → {:.1f}°C'.format(t, (t - 32) * 5/9))
    elif pergunta2 == 'k':
        print('Resultado da conversão: {}°F → {:.1f}°K'.format(t, (t - 32) * 5/9 + 273.15))

elif pergunta == 'k':
    if pergunta2 == 'c':
        print('Resultado da conversão: {}°K → {:.1f}°C'.format(t, t - 273.15))
    elif pergunta2 == 'f':
        print('resultado da conversão: {}°K → {:.1f}°F'.format(t, (t - 273.15) * 9/5 + 32 ))

print('-------------------------------------------')
