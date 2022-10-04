print('-' * 12)
print('--CALCULANDO--DESCONTOS!--')
nome = str(input('Nome:')).strip()
is_mecanic = str(input('Ele é mecânico:')).strip()
valor = float(input('Qual valor da compra:'))
if is_mecanic == 'sim':
    discount_value = valor - (valor * 10 / 100) 
    print(f'O valor com desconto fica por: R${discount_value:.2f}')
else: 
    discount_value = valor - (valor * 5 / 100)
    print(f'O valor com desconto fica por: R${discount_value:.2f}')

