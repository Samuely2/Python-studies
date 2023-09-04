#Escrever um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exibir os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período

#O programa está pedindo para exibir o valor final somando os juros por 24 meses

depositoInicial = float(input("Digite o depósito inicial: "))
taxaJuros = float(input("Digite a taxa de juros: "))


c = 1
aumentoJuros = 0
saldo = depositoInicial

while c <= 24:
    c = c + 1
    saldo = saldo + (saldo * (taxaJuros / 100))
    print(f"Saldo de {saldo:5.2f} no mês {c}")
    
