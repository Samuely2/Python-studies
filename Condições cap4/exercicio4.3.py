### Escreva um programa que leia três números e que imprima o maior valor e o menor

a = int (input("Digite o primeiro número")) 
b = int (input("Digite o segundo número"))
c = int (input("Digite o terceiro número"))

num = 0
menornum = 0

if num < a:

    num = a
    
if num < b:

    num = b

if num < c:

    num = c

if a > 0:

    menornum = a

if b < a:

    menornum = b

if c < b:

    menornum = c

print (f"O menor número é {menornum}")
print (f"O maior número é {num}")


