while True:
    opcoes = int(input("1- Soma | 2- Subtracao | 3- Multiplicacao | 4- Divisao | 5- Sair: "))
    
    if opcoes == 5:
        break
    
    tabuada = 1
    
    while tabuada <= 10:
        numero = 1
        
        while numero <= 10:
            if opcoes == 1:
                print(f"{tabuada} + {numero} = {tabuada + numero}")
            elif opcoes == 2:
                print(f"{tabuada} - {numero} = {tabuada - numero}")
            elif opcoes == 3:
                print(f"{tabuada} * {numero} = {tabuada * numero}")
            elif opcoes == 4:
                print(f"{tabuada} / {numero} = {tabuada / numero}")
            
            numero += 1
        
        tabuada += 1
