###Tabuada com inicio e fim

num = int (input("Digite o número"))
inicio = int (input("Digite o início")) #num 5 // inicio 5, fim 10. 
fim = int (input("Digite o fim"))  #fim 10 5x5 , 5x7, 5x8, 5x9, 5x10

multi = 0
while inicio <= fim:
    print(f"{inicio}" "*" f"{num}" "=" f"{multi}")
    inicio = inicio + 1
    multi = num * inicio







    