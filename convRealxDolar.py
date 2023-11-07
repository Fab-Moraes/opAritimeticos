def converterParaDolar(dinheiroNaCarteira, taxaDeCambio):
    return dinheiroNaCarteira / taxaDeCambio

taxaDeCambio = 3.27

dinheiroNaCarteira = float(input('Quanto você tem na carteira? '))
conv_Dolar = converterParaDolar(dinheiroNaCarteira, taxaDeCambio)

print(f'Com o valor que você tem, conseguirá comprar {conv_Dolar: .2f} Dólares')