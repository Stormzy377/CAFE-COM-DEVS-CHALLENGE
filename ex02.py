# Algoritmo que analisa e diz se um número é primo ou não

numero = int(input("Digite um número para verificar se é primo: "))
e_primo = True

if numero <= 1:
    e_primo = False

else:
    #Testar se qualquer outro número é divisível por 2 e ele mesmo
    for i in range(2, numero):
        if numero % i == 0:
            e_primo = False
            break
if e_primo:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")