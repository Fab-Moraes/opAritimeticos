'''Aqui será aplicado um desconto de 5% sobre o preço do produto'''

produto01 = float(input('Digite o preço atual do produto: '))

desconto01 = float(input('Quantos % você quer aplicar de desconto no produto? Ex. 2, 4, 6, 7...  ' ))

descProduto = (produto01 * desconto01) / 100 

print(f'Aqui está o valor do produto com o desconto: R$ {produto01 - descProduto:.2f}')
