'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

valorPorHora = float(input("Digite o valor recebido por hora: "))
numeroDeHoras = float(input("Digite a quantidade de horas trabalhadas no mês: "))
totalSalarial = valorPorHora*numeroDeHoras

print(f"O seu salário é: {totalSalarial:.0f}")
