##Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

valorDivida = float(input("Valor inicial da dívida: "))
taxa = int(input("Digite os juros mensais em porcentagem: "))
valorMensal = float(input("Digite o valor mensal que será pago: "))

meses = 0
totalpago = 0
juros = 0

# Converta a taxa de juros de porcentagem para decimal
taxa = taxa / 100.0

if (valorDivida * (taxa / 100) > valorMensal):
    print("O juros não pode ser superior ao pagamento mensal")

else:

    while valorDivida > valorMensal:
        meses = meses + 1
        valorDivida = valorDivida + taxa - valorMensal
        totalpago = totalpago + valorMensal + valorDivida
        juros = juros + valorDivida + taxa - valorMensal
           

    print(f"foi pago o total de {totalpago:.2f} com juros de R${juros} em {meses} meses")
