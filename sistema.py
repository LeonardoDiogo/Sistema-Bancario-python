menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q]Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 3
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é invalido. ")

    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou voce nao tem saldo suficiente. ")
        elif excedeu_limite:
            print("operação falhou! o valor do saque excede o limite. ")
        elif excedeu_saque:
            print("Operaçao falhou! numero maximo de saque excedido. ")

        elif valor > 0:
            saldo -= valor
            extrato -= f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! o valor informado é invalido")

    elif opcao == "e":
        print("\n=================== EXTRATO =====================")
        print("nao foram realizadas movimentaçoes. " if not extrato else extrato)
        print(f"\n saldo: R${saldo:2f}")
        print("===================================================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada. ")
