#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

num1 = int (input("Digite o primeiro número"))
num2 = int (input("Digite segundo número"))
result = 0
categoria = int(input("Digite 1 para soma, 2 para subtração, 3 para multiplicação, 4 para divisão"))

if categoria == 1:
    result = num1 + num2

elif categoria == 2:
    result = num1 - num2

elif categoria == 3:
    result = num1 * num2

elif categoria == 4:
    result = num1 / num2
else:
    print("Número inválido, digite entre 1 e 4")
    
print(f"O resultado desses dois valores são: {result}")  

##A indetação é importante, porque se eu desse um tab no segundo print para da o espaço, não daria certo por conta do else.
      

    