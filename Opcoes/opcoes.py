from Estoque.estoque import carregar_produtos
from Carrinho.carrinho import Carrinho_compras
from Verificador.verificar import verifica_opcao, forma_pagamento

produtos, tamanho_estoque = carregar_produtos("Estoque/produtos.csv") # Carrega os produtos do arquivo csv
carrinho_compras = Carrinho_compras() # Cria uma instância da classe para gerenciar o carrinho de compras

def opcoes(continuar):
    while True:
        try:
            print("\n1. Comprar produtos")
            print("2. Ver carrinho")
            print("3. Concluir compra")
            print("4. Sair")
            opcao = int(input("\nEscolha uma opção: ")) # Solicita ao usuário que escolha uma opção e converte para um número inteiro
            verifica_opcao(opcao) # Verifica se a opção escolhida é válida
            
            if opcao == 1:
                codigo = input("Digite o código do produto: ")
                if isinstance(codigo, int): # Verifica se o código digitado é um número inteiro
                    raise TypeError("Escolha um dos produtos disponíveis!\n")
                elif 1 <= int(codigo) <= tamanho_estoque: # Verifica se o código está dentro do intervalo válido do estoque
                    quantidade = int(input("Digite a quantidade: "))
                    carrinho_compras.adicionar_produtos(produtos, codigo, quantidade) # Adiciona o produto ao carrinho de compras
                else:
                    raise ValueError("O produto está fora de estoque!\n")
                
            elif opcao == 2:
                carrinho_compras.mostrar_carrinho(produtos) #Mostra o atual estado do carrinho de compras
                
            elif opcao == 3:
                total = carrinho_compras.calcular_total(produtos)
                if total > 0: #Verifica se o carrinho não esta vazio
                    print("Total da compra: R$", total)
                    print("\n")
                    pagamento = forma_pagamento(produtos)
                    carrinho_compras.nota_fiscal(produtos, "Nota_Fiscal.csv", pagamento) #Gera a nota fiscal da compra
                    nova_compra = input("\nSe deseja realizar outra compra tecle letra 'y': ")
                    if nova_compra == "Y" or nova_compra == "y": #Verifica se quer comprar novamente
                        pass
                    else:
                        return False
                else:
                    print("O carrinho está vazio! Por favor selecione os produtos desejados.")
                
            elif opcao == 4:
                print("Compra cancelada. Saindo do sistema...")
                return False
            
        except ValueError as erro:
            print("\nErro!", str(erro))
        except Exception as erro:
            print("\nErro inesperado!", str(erro))