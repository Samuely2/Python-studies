# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se e que podemos entender a multiplicação dos dois números como somas sucessivas de um deles.
#Assim 4x5 = 5+5+5+5 = 4x4x4x4x4

num1 = int (input("Digite o primeiro número"))
num2 = int (input("Digite o segundo número"))

c = 0
i = 0

if (num1 < num2):
    while (i < num1):
        i = i + 1
        c = c + num2
    print (f"{num1}" "x" f"{num2}" "=" f"{c}")
        
else:
    while (i < num2):
        i = i + 1
        c = c + num1
    print (f"{num1} " "x " f"{num2} " "= " f"{c}")
        
             





   
    


    