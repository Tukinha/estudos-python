'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius'''
fahre = float(input("Digite o valor em Fahrenheit: "))
trasformacaoParaCelsius = fahre-32/1.2
print(f"O resultado da conversão foi: {trasformacaoParaCelsius:.1f}°f")