menu = """
########## MENU ##########
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair
"""
saldo = 0.00
limite_saque = 500.00
numero_saques = 0
LIMITE_DIARIO = 3
extrato = ""
verificador = 0

while True:
    opcao = input(menu)
    if opcao == 'd':
        deposito = float(input("Digite o valor que deseja depositar: R$ "))
        if deposito < 0:
            print("Valor incorreto!")
        else:
            saldo += deposito
            extrato += "Depósito no valor de R$ " + str(f"{deposito:.2f}") + "\n"
            print("\nDepósito realizado com sucesso!")
            verificador += 1
    elif opcao == 's':
        if numero_saques < LIMITE_DIARIO:
            saque = float(input("Digite o valor que deseja sacar: R$ "))
            if saque > limite_saque:
                print("Limite de valor por saque excedido!")
            elif saque > saldo:
                print("Não será possível sacar o dinheiro por falta de saldo")
            else:
                saldo -= saque
                extrato += "Saque no valor de R$ " + str(f"{saque:.2f}") + "\n"
                print("\nSaque realizado com sucesso!")
                verificador += 1
                numero_saques += 1
        else:
            print("Limite de saques diários atingido!")
    elif opcao == 'e':
        if verificador == 0:
            print("Não foram realizadas movimentações")
        else:
            print("Aqui está o seu Extrato Bancário:")
            print(f"{extrato}Saldo da conta é: R$ {saldo:.2f}")
    elif opcao == 'q':
        break
    else:
        print("Opção inválida, por favor selecionar novamente a opção desejada.")