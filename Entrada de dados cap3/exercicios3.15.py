cigarros = int(input("Digite a quantidade de cigarros fumados por dia"))

anos = int(input("Quantos anos você ja fumou?"))

dias = anos * 365 ## convertendo os anos em dias
quantidadecigarros = cigarros * dias ## aq recebe o total geral de cigarros
minutos = dias * 24 * 60 ##ja tenho os minutos total
totalperdaminutos = quantidadecigarros * 10  ## aqui eu recebo os minutos totais de perda

novominuto = minutos - totalperdaminutos ## aqui eu eu recebo os minutos que sobraram com as perdas

novosdias = novominuto / 1440 ## e aqui e a conversão para dias dos minutos que sobraram

 
print(f"Você perderá {novosdias:.2f} dias de vida")