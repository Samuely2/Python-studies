mercadoria = int(input("Digite o valor da mercadoria"))
desconto = int(input("Digite o valor em percentual do desconto"))

valordodesconto = mercadoria * desconto / 100
novovalor = mercadoria - valordodesconto
print(f"O novo valor é :{novovalor}")