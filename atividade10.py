'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''
# ALGORITIMO:
primeiroNumeroInteiro = int(input("Digite o primeiro número inteiro: "))
segundoNumeroInteiro = int(input("Digite o segundo número inteiro: "))
numeroReal = float(input("Digite um número real: "))
dobroDoPrimeiroMaisMetadeDoSegundo = primeiroNumeroInteiro*2+segundoNumeroInteiro/2
somaDoTriploDoPrimeiroComOTerceiro = primeiroNumeroInteiro*3 + numeroReal
triploDoTerceiro = numeroReal**3
#SAIDA DE DADOS:
print(f"O produto do dobro do primeiro com a metade do segundo é: {dobroDoPrimeiroMaisMetadeDoSegundo}")
print(f"A soma do triplo do primeiro com o terceiro é: {somaDoTriploDoPrimeiroComOTerceiro}")
print(f"O terceiro elevado ao cubo é: {triploDoTerceiro:.2f}")

