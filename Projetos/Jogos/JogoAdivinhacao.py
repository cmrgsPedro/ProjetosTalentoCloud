import random

def jogar_adivinhacao():
    # Interface do jogo
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100")

    alvo = random.randint(1, 100)

    def verificar_chute(chute):
        try:
            chute = int(chute)
            
            if chute == alvo:
                return "Parabéns! Você acertou o número!"
            
            if chute > alvo:
                return f"O número é menor que {chute}. Tente novamente!"
            else:
                return f"O número é maior que {chute}. Tente novamente!"
                
        except ValueError:
            return "Por favor, digite um número válido!"

    while True:
        entrada = input("Digite seu chute (ou 'sair' para encerrar): ")

        if entrada.lower() == 'sair':
            print("Obrigado por jogar!")
            break
        
        resultado = verificar_chute(entrada)
        print(resultado)
        
        if "Parabéns" in resultado:
            jogar_novamente = input("Quer jogar novamente? (s/n): ")
            if jogar_novamente.lower() != 's':
                print("Obrigado por jogar!")
                break
            else:
                alvo = random.randint(1, 100)
                print("\nNovo jogo começou! Adivinhe o número entre 1 e 100")