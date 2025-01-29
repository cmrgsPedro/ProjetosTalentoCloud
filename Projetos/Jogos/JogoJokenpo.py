import random

def jogar_jokenpo():
    # Interface do jogo
    print("Bem-vindo ao jogo de Jokenpo!")
    print("Escolha entre pedra, papel e tesoura:\n")

    maos = ['pedra', 'papel', 'tesoura']

    jogada = input("Digite sua jogada: ")

    # Função para verificar a jogada
    def verificar_jogada(jogada):
        jogada = jogada.lower()
        
        if jogada not in maos:
            return "Por favor, escolha uma jogada válida!"
        
        computador = random.choice(maos)
        
        if jogada == computador:
            return f"Computador: {computador}\nEmpate! Ambos escolheram {jogada}"
        
        if jogada == 'pedra':
            if computador == 'papel':
                return f"Computador: {computador}\nVocê perdeu! {computador} cobre {jogada}"
            else:
                return f"Computador: {computador}\nVocê ganhou! {jogada} quebra {computador}"
        
        if jogada == 'papel':
            if computador == 'tesoura':
                return f"Computador: {computador}\nVocê perdeu! {computador} corta {jogada}"
            else:
                return f"Computador: {computador}\nVocê ganhou! {jogada} cobre {computador}"
        
        if jogada == 'tesoura':
            if computador == 'pedra':
                return f"Computador: {computador}\nVocê perdeu! {computador} quebra {jogada}"
            else:
                return f"Computador: {computador}\nVocê ganhou! {jogada} corta {computador}"

    print(f"\njo...\nken...\npô!\n")
    print(f"Você: {jogada}")
    print(verificar_jogada(jogada))