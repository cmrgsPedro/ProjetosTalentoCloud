## Desenvolvimento 3 ##

# 1a Forma
andar = []

for i in range(1,21):
    andar.append(i)
    if i == 13:
        andar.remove(i)
    
print(f"andares disponiveis: {andar}\n")

# 2a Forma
andares = []
qtdAndares = 20
j = 1

while j <= qtdAndares:
    andares.append(j)
    if j == 13:
        andares.remove(j)
    j += 1


print(f"andares disponiveis: {andares}\n")

# Desafio
inv = []

for k in range(1, len(andar) + 1):
    inv.append(andar[-k])
    
print(f"Andares invertidos: {inv}")