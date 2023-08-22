saldo = 0
deposito = 0
saque = 0
limite_saque = 500
LIMITE_DIARIO = 3
extrato = ""





while True:

    opcao = input("""
      ===========MENU===========

        [d]- DEPÓSITO

        [s] - SAQUE
                  
        [e] - EXTRATO
                  
        [q] - SAIR
                        
      ==========================
        """)
    

    if opcao == "d":
        print("============Deposito===========")#
        deposito = float(input("Quanto você deseja depositar? \n"))
            
        if deposito > 0 :
            saldo = saldo + deposito
            print(f"Foi adicionado R${deposito:.2f} à sua conta ")#
            extrato += f"Deposito de R${deposito:.2f} efetuado\n"
        else:
            print("Valor invalido")

    elif opcao == "s":
       
        print("=========Saque========")
        

        if LIMITE_DIARIO > 0 :
            
            saque = float(input("Quanto vc deseja sacar ?\n"))
            
            if saque > 500:
                print("Limite maximo é de R$500,00")
            else:
                
                if saque > saldo:
                    print("Saldo insuficiente")
                else:
                    saldo = saldo - saque
                    print(f"O saque de R${saque:.2f} foi efetuado com sucesso") 
                    extrato += f"Saque de R${saque:.2f} efetuado\n"
                    LIMITE_DIARIO = LIMITE_DIARIO - 1
                    print(f"Você ainda tem {LIMITE_DIARIO} saques disponiveuis")
        
        else:
            print("Limite diario de saque excedido")
            

    elif opcao == 'e':
        print("==========EXTRATO=========")
        print(extrato)
        (print(f"Seu saldo atual é de R${saldo:.2f}"))
    
    elif opcao == "q":
        break

    else:
        print("Opçao invalida")