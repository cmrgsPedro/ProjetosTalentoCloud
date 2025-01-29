# Adiciona o caminho das pastas dos jogos ao sys.path
from Jogos.JogoAdivinhacao import jogar_adivinhacao as adivinhacao
from Jogos.JogoJokenpo import jogar_jokenpo as jokenpo


# Interface do console
def exibir_menu():
    print("\nBem-vindo ao Console de Jogos!")
    print("Escolha o jogo que deseja jogar:")
    print("1 - Jogo de Adivinhação")
    print("2 - Jogo de Jokenpo")
    print("3 - Sair")

def main():
    while True:
        exibir_menu()
        escolha = input("Digite o número do jogo: ").strip()

        if escolha == '1':
            adivinhacao()
        elif escolha == '2':
            jokenpo()
        elif escolha == '3':
            print("Obrigado por jogar!")
            break
        else:
            print("Por favor, escolha uma opção válida!")

if __name__ == '__main__':
    main()