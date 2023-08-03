'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''
#ENTRADA DE DADOS:
primeiro_numero_inteiro = int(input("Digite o primeiro número inteiro: "))
segundo_numero_inteiro = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))
#PROCESSAMENTO DE DADOS:
produto_do_dobro_do_primero_com_a_metade_do_segundo = primeiro_numero_inteiro*2+segundo_numero_inteiro/2
soma_do_triplo_do_primeiro_com_o_terceiro = primeiro_numero_inteiro*3 + numero_real
terceiro_ao_cubo = numero_real**3
#SAIDA DE DADOS:
print(f"O produto do dobro do primero com a metade do segundo é: {produto_do_dobro_do_primero_com_a_metade_do_segundo}")
print(f"A soma do triplo do primeiro com o terceiro é: {soma_do_triplo_do_primeiro_com_o_terceiro:.2f}")
print(f"O terceiro elevado ao cubo é: {terceiro_ao_cubo:.2f}")


