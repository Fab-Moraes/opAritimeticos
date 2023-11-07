numero = int(input('Digite um numero para eu criar a sua Tabuada: '))

# Loop de 1 a 10 para criar a tabuada

for i in range(1, 11):
    resultado = numero * 1
    print(f'{numero} x {i} = {resultado}')