#Exercício que mostra a tabuáda de um número de 1 a 12

numero = int(input("Digite um número para ver a tabuáda: "))

for i in range(1, 13):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")