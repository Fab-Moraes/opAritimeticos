# Calcular a quantidade de tinta para pintar uma parede

print('Me forneça os seguintes dados (em metros): ')

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura? '))

areaDaParede = altura * largura

umLitroTinta_m2 = 6

print(f'A área total da parede é igual a: {areaDaParede:.2f} m², serão necessários '
      f'{areaDaParede / umLitroTinta_m2:.3f} litros de tinta para pintar toda a parede!')
