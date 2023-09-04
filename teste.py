valorDivida = float(input("Valor inicial da dívida: "))
taxa = float(input("Digite os juros mensais em porcentagem: "))
valorMensal = float(input("Digite o valor mensal que será pago: "))

meses = 0
totalpago = 0
juros = 0

# Converta a taxa de juros de porcentagem para decimal
taxa = taxa / 100.0

if (valorDivida * taxa > valorMensal):
    print("Os juros não podem ser superiores ao pagamento mensal")
else:
    while valorDivida > 0:
        meses = meses + 1
        juros_mes = valorDivida * taxa
        valorDivida = valorDivida + juros_mes - valorMensal
        totalpago = totalpago + valorMensal
        juros = juros + juros_mes

    print(f"Foi pago um total de R${totalpago:.2f} com juros de R${juros:.2f} em {meses} meses")
