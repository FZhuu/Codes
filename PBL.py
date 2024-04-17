# variáveis numéricos
saldo = 0
valor_passagem = 0
contador = 0
# variáveis True|False
adcional = True
menu_usu = True
menu_senha_usu = True
menu_adm_senha = True
menu_adm = True
# início do sistema
while True:
    # retorno das variáveis a True após declarar falso no meio do código
    adcional = True
    menu = True
    menu_senha_usu = True
    menu_adm_senha = True
    menu_1 = True
    # retorno do contador(tentativas da senha) a 0 
    contador = 0
    # opções de entrada
    print("============= Opções de contas =============")
    print("Opções de contas")
    print("1 = Usuário")
    print("2 = Administrador")
    print("3 = Sair")
    print("============================================")
    conta = input("Digite qual conta deseja utilizar: ").strip()
    # opção usuário escolhido
    if conta == "1" :
        print("\nBem vindo a página de login do usuário. ")
        # input da senha
        while menu_senha_usu:
            senha1 = input("\nPara continuar, por favor, digite a senha: ")
            while contador <= 2:
                if senha1 == "123456":
                    contador = 0
                    print("\nBem vindo a página do Usuário!")
                    # opções do usuário
                    while menu_usu:
                        adcional = True
                        print("\n============== Opções de menu ==============")
                        print("1 = Usar cartão")
                        print("2 = Recarregar saldo")
                        print("3 = sair")
                        print("============================================")
                        opcao_usuario = input("Digite a opção que deseja utilizar: ").strip()
                        # opção uso do cartão
                        if opcao_usuario == "1":
                            if saldo < valor_passagem:
                                print("\n============================================")
                                print("\nSaldo insuficiente.")
                                print("\n Seu saldo atual é de:",saldo)
                                print("\n============================================")
                            else:
                                print("\n============================================")
                                print("\nValor da passagem debitado do cartão")
                                saldo -= valor_passagem
                                print("\nSeu saldo atual é de:",saldo)
                                print("\n============================================")
                            continue
                        # opção adicionar saldo
                        elif opcao_usuario == "2":
                            while adcional:
                                add_saldo = input("\nDigite quanto deseja recarregar: ").strip()
                                if add_saldo.isalpha():
                                    print("\nCarácter inválido")
                                    print("\n============================================")
                                    continue
                                if add_saldo:
                                    saldo += float(add_saldo)
                                    print("Saldo após a recarga:",saldo)
                                    adcional = False
                                else:
                                    print("\nCaracter não identificado.")
                                    print("Tente novamente.")
                            continue
                        # opção sair da página do usuário
                        elif opcao_usuario == "3":
                            print("\n===========================================")
                            print("Voltando para página inicial")
                            menu_senha_usu = False
                            menu_usu = False
                            break
                        else:
                            print("============================================")
                            print("\nOpção inválida.")
                            print("Tente novamente.")
                            print("\n============================================")
                            continue   
                else:
                    contador += 1
                    print("\nSenha incorreta. Tentativas restantes:", 3 - contador)
                    if contador == 3:
                        menu_senha_usu = False
                        print("\nNúmero máximo de tentativas excedido.")
                        break
                break
    # opção administrador
    elif conta == "2" :
        print("\nBem vindo a página de login do administrador. ")
        # input da senha
        while menu_adm_senha:
            senha_adm = input("\nPara continuar, por favor digite a senha de administrador: ")
            while contador <= 2 :
                if senha_adm == "123456":
                    contador == 0
                    # opções administrador
                    while menu_adm:
                        print("\nBem vindo a página do administrador")
                        print("\n============== Opções de menu ==============")
                        print("1 = definir preço da passagem")
                        print("2 = ver saldo")
                        print("3 = sair")
                        print("============================================")
                        opcao_adm = input("Digite a opção que deseja utilizar: ").strip()
                        # opção redefir valor da passagem
                        if opcao_adm == "1":
                            while True:
                                change_passagem = input("\ndigite o valor da passagem")
                                if change_passagem.isnumeric():
                                    valor_passagem = float(change_passagem)
                                    if valor_passagem > 0:
                                        break
                                else:
                                    print("\nDigite um número válido.")
                        # opção consultar saldo do usuário
                        elif opcao_adm == "2":
                            print("============================================")
                            print("\nSaldo atual:",saldo)
                            print("\n============================================")
                        # opção sair da página do administrador
                        elif opcao_adm == "3":
                            menu_adm = False
                            menu_adm_senha = False
                            break
                        else:
                            print("============================================")
                            print("\nOpção inválida.")
                            print("Tente novamente.")
                            print("\n============================================")
                            continue
                    break    
                else:
                    contador += 1
                    print("\nSenha incorreta. Tentativas restantes:", 3 - contador)
                    if contador == 3:
                        menu_adm_senha = False
                        print("\nNúmero máximo de tentativas excedido.")
                        break
                break   
    # opção encerrar código
    elif conta == "3":
        print("\nSistema encerrado.")
        break
    else: 
        print("Por favor, escolha entre as opções oferecidas. ")