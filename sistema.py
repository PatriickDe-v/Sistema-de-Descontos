print('-' * 12)
print('--CALCULANDO--DESCONTOS!--')
nome = str(input('Nome:')).strip()
cliente = str(input('Ele é mecânico:')).strip()
valor = float(input('Qual valor da compra:'))
if cliente == 'sim':
    descon = valor - (valor * 10 / 100) 
    print(f'O valor com desconto fica por: R${descon:.2f}')
else: 
    descon = valor - (valor * 5 / 100)
    print(f'O valor com desconto fica por: R${descon:.2f}')

