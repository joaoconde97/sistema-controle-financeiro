def asteriscos():
    print(30 * "*")

def mostrar_menu():

    asteriscos()
    print("             MENU")
    asteriscos()
    print("1 - Adicionar receita ")
    print("2 - Adicionar despesa")
    print("3 - Ver saldo atual ")
    print("4 - Ver histórico ")
    print("5 - Sair ")
    asteriscos()

def pedir_valor():
    while True:
        try:
            valor = float(input("Digite o valor: "))
            return valor
        
        except ValueError:
            print("Valor inválido, digite um número.")

def adicionar_registros(registros, tipo):
    valor = pedir_valor()
    descricao = input("Descrição: ")

    registro = {
        "tipo" : tipo,
        "valor" : valor,
        "descricao" : descricao
    }

    registros.append(registro)

registros = []

while True:

    mostrar_menu()

    opcao = input("Digite a opção desejada: ")
    
    if opcao.isdigit():

        if opcao == "1":
            adicionar_registros(registros, "receita")

        elif opcao == "2":
            adicionar_registros(registros, "despesa")

        elif opcao == "3":
            print("Voce escolheu 3")
        elif opcao == "4":
            print("Voce escolheu 4")
        elif opcao == "5":
            print("\n Encerrando programa... \n")
            break
        else:
            print()
            print("Opção Inválida, tente novamente!")
            print()

    else:
        print()
        print("Opção Inválida, tente novamente!")
        print()