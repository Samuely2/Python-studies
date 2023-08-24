### Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superior a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%

salario = float(input("Digite o seu salário"))

base = salario
aumento = 0.0

if base >= 1250.00:
    aumento = base * 0.10
    print(f"Seu salário é de {base} com aumento de ${aumento:.2f} ficando {base+aumento}")
    
if base < 1250.00:
    aumento = base * 0.15
    print(f"Seu salário é de {base} com aumento de ${aumento:.2f} ficando {base+aumento}")
