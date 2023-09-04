# Alterar o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte

depositoInicial = float(input("Digite o depósito inicial: "))
taxaJuros = float(input("Digite a taxa de juros: "))
depositoMensal = float (input("Digite o valor do depósito mensal"))


c = 1
aumentoJuros = 0
saldo = depositoInicial

while c <= 24:
    c = c + 1
    saldo = saldo + (saldo * (taxaJuros / 100)) + depositoMensal
    print(f"Saldo de {saldo:.2f} no mês {c}")
    