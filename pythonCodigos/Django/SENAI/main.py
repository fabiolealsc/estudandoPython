dados = [{"Nome": "Fabio", "Idade": 26, "Wats": 995456},
         {"Nome": "Pedro", "Idade": 34, "Wats": 596859},
         {"Nome": "Luiz", "Idade": 65, "Wats": 657444},
         {"Nome": "Marcos", "Idade": 45, "Wats": 666675},
         {"Nome": "Eneas", "Idade": 35, "Wats": 345677}]
opc = 7


def cab(n=10):
    print()
    print("#" * n)


def opcoes(opc):
    if opc == 1:
        x = "Nome"
        y = "Idade"
        z = "Wats"
    elif opc == 2:
        x = "Idade"
        y = "Nome"
        z = "Wats"
    elif opc == 3:
        x = "Idade"
        y = "Wats"
        z = "Nome"
    elif opc == 4:
        x = "Wats"
        y = "Idade"
        z = "Nome"
    elif opc == 5:
        x = "Wats"
        y = "Nome"
        z = "Idade"
    else:
        x = "Nome"
        y = "Wats"
        z = "Idade"
    return x, y, z


while opc > 6:
    opc = int(input("1 - NOME, IDADE, WATS\n"
                    "2 - IDADE, NOME, WATS\n"
                    "3 - IDADE, WATS, NOME\n"
                    "4 - WATS, IDADE, NOME\n"
                    "5 - WATS, NOME, IDADE\n"
                    "6 - NOME, WATS, IDADE\n"
                    "\nEscolha a ordem de mostragem: "))


cab(40)
print(f"{opcoes(opc)[0]:<9}", f"{opcoes(opc)[1]:<9}", opcoes(opc)[2])
for i in dados:
    print(f"{i.get(opcoes(opc)[0]):<10}", end="")
    print(f"{i.get(opcoes(opc)[1]):<10}", end="")
    print(f"{i.get(opcoes(opc)[2]):<10}", end="")
    print()
