import textwrap

def menu():
    menu = """
    ########## MENU ##########
        [u] - \tCriar novo usuário
        [c] - \tCriar conta corrente
        [l] = \tListar contas
        [d] - \tDepositar
        [s] - \tSacar
        [e] - \tExtrato
        [q] - \tSair
    ##########################
    """
    print(menu)

def opcao_deposito(saldo, valor, extrato, verificador, /):
    if valor < 0:
            print("Valor incorreto!")
    else:
            saldo += valor
            extrato += "Depósito no valor de R$ \t" + str(f"{valor:.2f}") + "\n"
            print("\n##### Depósito realizado com sucesso! #####")
            verificador += 1
    return saldo, extrato, verificador

def opcao_saque(*, saldo, valor, extrato, limite_saque, numero_saques, LIMITE_DIARIO, verificador):
    if (numero_saques >= LIMITE_DIARIO):
        print("Limite de saques diários atingido!")
    elif valor > limite_saque:
        print("Limite de valor por saque excedido!")
    elif valor > saldo:
        print("Não será possível sacar o dinheiro por falta de saldo")
    else:
        saldo -= valor
        extrato += "Saque no valor de R$ \t" + str(f"{valor:.2f}") + "\n"
        print("\n##### Saque realizado com sucesso! #####")
        verificador += 1
        numero_saques += 1
    return saldo, extrato, numero_saques, verificador

def opcao_extrato(saldo, /, *, extrato, verificador):
    if verificador == 0:
        print("Não foram realizadas movimentações")
    else:
        print("Aqui está o seu Extrato Bancário:\n")
        print(f"{extrato}Saldo da conta é: R$ {saldo:.2f}")
        
def cria_usuario(usuarios):
    nome = input("Nome Completo: ")
    data_nascimento = input("Data de Nascimento (Formato DD/MM/YYYY): ")
    CPF_lista = list(input("CPF: "))
    for i in CPF_lista:
        if (i == '.'):
            CPF_lista.remove('.')
        elif(i == '-'):
            CPF_lista.remove('-')    
    CPF = ''.join(CPF_lista)
    endereco = input("Endereço:")
    for i in usuarios:
        if(i["cpf"] == CPF):
            print("\nCPF já cadastrado")
            return
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": CPF, "endereco": endereco})
        

def criar_conta(agencia, numero_conta, usuarios, contas):
    CPF = input("Informe o CPF do usuário: ")
    for i in usuarios:
        if(i["cpf"] != CPF):
            print("\nCPF não encontrado")
            return
        else:
            print("\n=== Conta criada com sucesso! ===")
            contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": i})
    

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))   
    

AGENCIA = "001"
saldo = 0.00
numero_saques = 0
extrato = ""
verificador = 0
usuarios = []
contas = []

while True:
    menu()
    opcao = input('=>')
    if opcao == 'u':
        cria_usuario(usuarios)
    elif opcao == 'c':
        numero_conta = len(contas) + 1
        criar_conta(AGENCIA, numero_conta, usuarios, contas)
    elif opcao == 'l':
        listar_contas(contas)
    elif opcao == 'd':
        saldo, extrato, verificador = opcao_deposito(saldo, float(input("Digite o valor que deseja depositar: R$ ")), extrato, verificador)
    elif opcao == 's':
        saldo, extrato, numero_saques, verificador = opcao_saque(saldo=saldo,valor = float(input("Digite o valor que deseja sacar: R$ ")), extrato=extrato, limite_saque=500, numero_saques=numero_saques,LIMITE_DIARIO=3, verificador=verificador)
    elif opcao == 'e':
        opcao_extrato(saldo, extrato=extrato, verificador=verificador)
    elif opcao == 'q':
        break
    else:
        print("Opção inválida, por favor selecionar novamente a opção desejada.")