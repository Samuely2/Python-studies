# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de KWh consumida e o tipo de instalação: R para residências, i para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir

quantidadekWh = int (input("Digite a quantidade de kWh consumida"))

instalacao = (input("Digite o tipo de instalação R - Residências, C - Comerciaol, I - Indústrias"))

preço = 0

if instalacao == "R":
    if quantidadekWh <= 500:
        preço = quantidadekWh * 0.40
    else:
        preço = quantidadekWh * 0.65
elif instalacao == "C":
    if quantidadekWh <= 1000:
        preço = quantidadekWh * 0.55
    else:
        preço = quantidadekWh * 0.60
elif instalacao == "I":
    if quantidadekWh <= 5000:
        preço = quantidadekWh * 0.55
    else:
        preço = quantidadekWh * 0.60

print(f"Você terá que pagar {preço:.2f}")