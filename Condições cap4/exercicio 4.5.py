
salario = float(input("Digite o seu salário"))

base = salario
aumento = 0.0

if base > 1250.00:
    aumento = base * 0.10
    print(f"Seu salário é de {base} com aumento de ${aumento:.2f} ficando {base+aumento}")
    
else:
    aumento = base * 0.15
    print(f"Seu salário é de {base} com aumento de ${aumento:.2f} ficando {base+aumento}")
