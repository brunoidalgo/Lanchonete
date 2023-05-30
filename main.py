print("----------Bem vindo a Lanchonete 1.0v-----------")
desejo = input("Deseja fazer um pedido? Digite (S/N): ")

if desejo.lower() == "s":
    print("----------Menu----------")
    print("|Código |         Produto        |    Preço    |")
    print("|   1   |         X-Tudo         |   R$15,00   |")
    print("|   2   |    Refrigerante Lata   |   R$4,00    |")
    print("|   3   |     Cachorro Quente    |   R$10,00   |")
    print("|   4   |     Suco de Laranja    |   R$5,00    |")
    print("|   5   |     Suco de Limão      |   R$5,00    |")
    print("|   6   |     Salgado Frito      |   R$5,00    |")
    print("|   7   |     Salgado Assado     |   R$7,00    |")
    print("|   8   |     Suco de Uva        |   R$4,00    |")
    print("|   9   |     Suco de Caju       |   R$7,00    |")
    print("|  10   |       X-Baccon         |   R$15,00   |")
    print("|  11   |         X-Egg          |   R$12,00   |")
    print("|  12   |       X-Salada         |   R$10,00   |\n")
    # \n -> é um caractere especial que representa uma nova linha,
    #  ou seja, imprime a linha do menu e passa para a próxima linha.

    acumulador = 0

    while True:
        codigo = input("Entre com o código desejado: ")
        if codigo == '1':
            acumulador += 15
        elif codigo == '2':
            acumulador += 4
        elif codigo == '3':
            acumulador += 10
        elif codigo == '4':
            acumulador += 5
        elif codigo == '5':
            acumulador += 5
        elif codigo == '6':
            acumulador += 5
        elif codigo == '7':
            acumulador += 7
        elif codigo == '8':
            acumulador += 4
        elif codigo == '9':
            acumulador += 7
        elif codigo == '10':
            acumulador += 15
        elif codigo == '11':
            acumulador += 12
        elif codigo == '12':
            acumulador += 10
        else:
            print('Código digitado inválido.')
            continue
        print('O valor a ser pago está em: R${:.2f}'.format(acumulador))
        resposta = input("Deseja fazer algum outro pedido? Digite (S/N): ")
        if resposta.lower() != "s":
            print('O valor final da conta é: R${:.2f}'.format(acumulador))
            print()
            print("1 - Cartão Debito")
            print("2 - Cartão Crédito")
            print("3 - Alimentação")
            print("4 - Refeição")
            print("5 - Dinheiro")
            print("6 - Pix")
            print()
            forma_pagamento = input("Qual será a forma de pagamento? ")

            if (forma_pagamento == "1"):
                print(
                    f"O valor de R${acumulador:.2f} será pago em Débito " .format(acumulador))
            elif (forma_pagamento == "2"):
                print(
                    f"O valor de R${acumulador:.2f} será pago em Crédito " .format(acumulador))
            elif (forma_pagamento == "3"):
                print(
                    f"O valor de R${acumulador:.2f} será pago em Vale Alimentação " .format(acumulador))
            elif (forma_pagamento == "4"):
                print(
                    f"O valor de R${acumulador:.2f} será pago em Vale Refeição " .format(acumulador))
            elif (forma_pagamento == "5"):
                print(
                    f"O valor de R${acumulador:.2f} será pago em Dinheiro " .format(acumulador))
            elif (forma_pagamento == "6"):
                print(
                    f"O valor de R${acumulador:.2f} será pago em Pix " .format(acumulador))

            verifica_pagamento = input("O pagamento foi feito ?")

            if verifica_pagamento.lower() == "s":
                print("Obrigado e volte sempre!")
            else:
                print("Por favor verificar pagamento com o cliente !")

            break
else:
    print("Obrigado e volte sempre!")


""" 
print('O valor a ser pago está em: {:.2f}'. format(acumulador))
        resposta = input("Deseja fazer algum outro pedido ? Digite (S/N)")
        while resposta == "S":
            codigo = input("Entre com o código desejado:")
            if (codigo == '1'):
                acumulador += 15
            elif (codigo == '2'):
                acumulador += 4
            elif (codigo == '3'):
                acumulador += 10
            elif (codigo == '4'):
                acumulador += 5
            else:
                print(
                    'O valor final da conta é: {:.2f} Qual será a forma de pagamento ?' . format(acumulador))
                break
"""
