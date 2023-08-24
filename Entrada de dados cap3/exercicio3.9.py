dias = int(input("Digite a quantidade de dias"))
horas = int (input("Digite a quantidade de horas"))
minutos = int (input("Digite a quantidade de minutos"))
segundos = int(input("Digite a quantidade em segundos"))

secdias = dias * 86400
sechoras = horas * 3600
secminutos = minutos * 60

total = secdias + sechoras + secminutos + segundos

print(f"O total em segundos é: {total}")