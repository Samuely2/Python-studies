kmpercorrido = float(input("Digite a quantidade km's percorridos"))

dias = int(input("Digite a quantidade de dias com o carro alugado"))

kmcalculo = kmpercorrido * 0.15

diacalculo = dias * 60

somafinal = kmcalculo + diacalculo
print(f"No total você irá pagar R${somafinal:.2f}")