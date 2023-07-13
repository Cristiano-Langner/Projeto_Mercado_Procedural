def verifica_opcao(opcao):
    if opcao < 1 or opcao > 4: # Verifica se a opção está fora do intervalo válido (1 a 4)
        raise ValueError("Escolha uma das opções disponíveis!\n")
    
def forma_pagamento(self):
    pagamento = int(input("1. Débito.\n2. Crédito.\n3. Dinheiro.\nInforme a forma de pagamento: "))
    if pagamento not in [1, 2, 3]:
        raise ValueError("Opção de pagamento inválida!")
    if pagamento == 1:
        print("Pagamento no débito selecionado.")
        print("Adicionado desconto de 5%!")
        print("Imprimindo NF...\n")
    elif pagamento == 2:
        print("Pagamento no crédito selecionado.") 
        print("Imprimindo NF...\n")
    elif pagamento == 3:
        print("Pagamento no dinheiro selecionado.")
        print("Adicionado desconto de 5%!")
        print("Imprimindo NF...\n")
    return pagamento # Retorna a opção de pagamento escolhida