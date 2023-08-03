import random

print("Aperte ctrl+c para sair")
while True:
    name = input("Nome do jogador: ")
    input("Role o dado(aperte qualquer coisa)")
    n = random.randint(0,6)

    print(name, " ,você rolou um ",n, "!")
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