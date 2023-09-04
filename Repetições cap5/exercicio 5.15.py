#Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto

#Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código inválido"

c = 0
preco = 0


while True:
    codProduto = int (input('Digite o código do produto ou 0 para cancelar'))
    if codProduto == 0:
        print(f"O total de compras foram {c} com o valor total de {preco}")
        break
    quantidadeComprada = int (input('Digite a quantidade comprada'))
    c += quantidadeComprada
    if codProduto == 1:
        preco += 0.50 * quantidadeComprada

    elif codProduto == 2:
        preco += 1.00 * quantidadeComprada
         
    elif codProduto == 3:
        preco += 4.00 * quantidadeComprada

    elif codProduto == 5:
        preco += 7.00 * quantidadeComprada

    elif codProduto == 9:   
        preco += 8.00 * quantidadeComprada
 




