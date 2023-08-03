import random

print("Digite break no campo de nome de jogador para sair")
while True:
    name = input("Nome do jogador: ")
    
    if(name == "break"): 
        print("Programa terminado. Obrigado por ter utilizado o rola dados. Até a próxima!")
        break

    input("Role o dado(aperte qualquer coisa)")
    
    n = random.randint(1,6)

    print(name, ", você rolou um ",n, "!")
    if(n == 1):
        print("[     ]", end="\n")
        print("[  0  ]", end="\n")
        print("[     ]", end="\n")
    elif(n == 2):
        print("[     ]", end="\n")
        print("[0   0]", end="\n")
        print("[     ]", end="\n")
    elif(n == 3):
        print("[     ]", end="\n")
        print("[0 0 0]", end="\n")
        print("[     ]", end="\n")
    elif(n == 4):
        print("[0   0]", end="\n")
        print("[     ]", end="\n")
        print("[0   0]", end="\n")
    elif(n == 5):
        print("[0   0]", end="\n")
        print("[  0  ]", end="\n")
        print("[0   0]", end="\n")
    else:
        print("[0   0]", end="\n")
        print("[0   0]", end="\n")
        print("[0   0]", end="\n")
