
salarioAntigo = float(input('Digite o salário atual do funcionário: '))

if salarioAntigo < 0:
    print('O salário não pode ser negativo.')
else:
    acrescimoSalario = float(input('Qual porcentagem de aumento gostaria de aplicar? Obs. somente numeral! '))

    if acrescimoSalario < 0:
        print('A porcentagem de aumento não pode ser negativa.')
    else:
        novoSalario = (acrescimoSalario * salarioAntigo) / 100 + salarioAntigo
        print(f'Aqui está o novo salário aplicado: R$ {novoSalario:.3f}')
