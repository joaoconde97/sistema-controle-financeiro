import json

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

            if valor < 0:
                print("O valor precisa ser maior que zero.")
                continue

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

    asteriscos()
    print(f"Tipo: {tipo}")
    print(f"Valor: {valor}")
    print(f"Descrição: {descricao}")
    asteriscos()

    confirmacao = input("Confirmar (s/n)? ")
    
    if confirmacao.lower().strip() == "s":
        registros.append(registro)
        salvar_registros(registros)
        return registros
    
    elif confirmacao.lower().strip() == "n":
        print("Registro cancelado.")
        return registros

    else:
        print("Opção inválida, tente novamente!")
        return registros

def salvar_registros(registros):
    local_arquivo = "C:\\Users\joaot\Documents\Estudos\Controle-financeiro\\registros.json"
    with open(local_arquivo,"w")as arquivo:
        json.dump(registros, arquivo, indent=4)

def carregar_registros():
    try:
        with open("registros.json", "r")as arquivo:
            return json.load(arquivo)

    except (FileNotFoundError, json.JSONDecodeError):
        return []

def main():
    registros = carregar_registros()

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


if __name__== "__main__":
    main()