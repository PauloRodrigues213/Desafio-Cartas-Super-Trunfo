import 

# Cartas de países com seus atributos
cartas = {
    "Brasil": {
    "População (milhões)": 215,
        "Área (milhões km²)": 8.5,
        "PIB (trilhões)": 1.9
    },
    "Estados Unidos": {
"População (milhões)": 331,
"Área (milhões km²)": 9.8, 
        "PIB (trilhões)": 25.5
    },
    "Japão": {
        "População (milhões)": 125,
        "Área (milhões km²)": 0.377,
        "PIB (trilhões)": 4.9
    },
    "Alemanha": {
        "População (milhões)": 83,
        "Área (milhões km²)": 0.357,
        "PIB (trilhões)": 4.3
    },
    "Índia": {
        "População (milhões)": 1400,
        "Área (milhões km²)": 3.3,
        "PIB (trilhões)": 3.7
    }
}

# Escolher uma carta para o jogador e uma para o computador
minha_carta = random.choice(list(cartas.keys()))
carta = random.choice([pais for pais in cartas if pais != minha_carta])

print("Bem-vindo ao Super Trunfo de Países!")
print("Sua carta é:", minha_carta)
print("Atributos disponíveis:")
print("1 - População (milhões)")
print("2 - Área (milhões km²)")
print("3 - PIB (trilhões)")
escolha = input("Escolha o número do atributo para competir: ")

# Comparar os valores
f escolha == "1":
    atributo = "População (milhões)"
elif escolha == "2":
    atributo = "Área (milhões km²)"
elif escolha == "3":
    atributo = "PIB (trilhões)"
else:
    print("Opção inválida.")
    exit()

valor = cartas[minha_carta][atributo]
valor pc = cartas[carta_pc][atributo]

print("\nVocê escolheu:", atributo)
print("Sua carta:", minha_carta, "-", atributo, "=",
print("Carta do computador:", carta_pc, "-", atributo, "=", valor_pc)

# Ver quem venceu
if valor_jogador valor_pc:
    print("\nParabéns! Você venceu!")
elif valor_jogador valor_pc:
    print("\nVocê perdeu. Tente novamente!")
else:
    print("\nEmpate!")
