'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''
celsius = float(input("Digite a temperatura em Celsius: "))
trasformaçãoParaFehrenheit = celsius*1.8+32
print(f'O valor da conversão é: {trasformaçãoParaFehrenheit:.1f}°f')