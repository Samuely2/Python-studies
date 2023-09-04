##Escrever um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética. 

c = 0
qntd = 0

while True:
    num = int (input("Digite um número"))
    qntd = qntd + 1 
    num = num + num
    if num == 0:
        break
    media = num / qntd
print (f"A quantidade de números digitados foram {qntd} com a média aritmética de {media}")