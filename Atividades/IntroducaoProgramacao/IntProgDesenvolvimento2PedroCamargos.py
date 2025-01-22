## Desenvolvimento 2 ##

# Caracteristicas veiculo
quantidade_rodas = int(input("Digite a quantidade de rodas: "))
peso_bruto = float(input("Digite o peso bruto do veículo (em kg): "))
quantidade_pessoas = int(input("Digite a quantidade de pessoas: "))

# Verifica a categoria da carteira
if quantidade_rodas == 2 or quantidade_rodas == 3:
    print("Categoria A")
elif quantidade_rodas == 4 and quantidade_pessoas <= 8 and peso_bruto <= 3500.0:
    print("Categoria B")
elif quantidade_rodas >= 4 and 3500.0 < peso_bruto <= 6000.0:
    print("Categoria C")
elif quantidade_rodas >= 4 and quantidade_pessoas > 8:
    print("Categoria D")
elif quantidade_rodas >= 4 and peso_bruto > 6000.0:
    print("Categoria E")
else:
    print("Categoria não identificada")