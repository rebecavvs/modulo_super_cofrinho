print("SUPER COFRINHO")
print("===================")

saldo = 0

def menu():
    print("\Escolha uma opção:")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

while True:
    menu()
    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        print(f"\Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "2":
        valor = float(input("Quanto deseja depositar? R$ "))
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado!")

    elif opcao == "3":
        valor = float(input("Quanto deseja sacar? R$ "))
        if valor <= saldo:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado!")
        else:
            print("Saldo insuficiente!")

    elif opcao == "4":
        print("Saindo... até a próxima!")
        break

    else:
        print("Opção inválida. Tente novamente.")
