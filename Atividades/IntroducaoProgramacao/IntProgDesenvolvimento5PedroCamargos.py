## Desenvolvimento 5 ##

def calculadora(num1, num2, op):
    try:
        num1 = float(num1)
        num2 = float(num2)
        op = int(op)
    except ValueError:
        return "Erro: insira apenas números"
    if op not in [1, 2, 3, 4, 0]:
        return "Erro: insira um operador válido"
    if op == 4 and num2 == 0:
        return "Erro: divisão por zero"
    
    # Realiza a operação de acordo com o operador
    match op:
        case 1:
            return num1 + num2
        case 2:
            return num1 - num2
        case 3:
            return num1 * num2
        case 4:
            return num1 / num2
        case 0:
            return 0

# Interface da calculadora
print("Calculadora\n")

while True:
    op = input("Digite o operador\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n0 - Sair\nop: ")
    
    if op == '0':
        print("Saindo da calculadora.")
        break
    else:
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")

    resultado = calculadora(num1, num2, op)
    print(f"\nResultado: {resultado}\n")