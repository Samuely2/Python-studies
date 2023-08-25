# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valorCasa = float (input("Digite o valor da casa"))
salario = float (input("Digite o seu salário"))
anos = int (input("Digite a quantidade de anos a pagar"))


LimiteP = salario * 0.30 ##Exemplo, se o salário for 1000, vai tirar o valor de 30% que é 300.
meses = anos * 12 

prestacao = valorCasa / meses

if prestacao <= LimiteP:

    print(f"O valor da prestação ficará R${prestacao:.2f}")

else:

    print (f"O valor da prestação está 30% acima do seu salário")
