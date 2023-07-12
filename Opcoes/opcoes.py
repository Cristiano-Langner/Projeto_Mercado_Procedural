from Estoque.estoque import carregar_produtos
from Carrinho.carrinho import Carrinho_compras
from Verificador.verificar import verifica_opcao, forma_pagamento

produtos, tamanho_estoque = carregar_produtos("Estoque/produtos.csv")
carrinho_compras = Carrinho_compras()

def opcoes(continuar):
    while True:
        try:
            print("\n1. Comprar produtos")
            print("2. Ver carrinho")
            print("3. Concluir compra")
            print("4. Sair")
            opcao = int(input("\nEscolha uma opção: "))
            verifica_opcao(opcao)
            
            if opcao == 1:
                codigo = input("Digite o código do produto: ")
                if isinstance(codigo, int):
                    raise TypeError("Escolha um dos produtos disponíveis!\n")
                elif 1 <= int(codigo) <= tamanho_estoque:
                    quantidade = int(input("Digite a quantidade: "))
                    carrinho_compras.adicionar_produtos(produtos, codigo, quantidade)
                else:
                    raise ValueError("O produto está fora de estoque!\n")
                
            elif opcao == 2:
                carrinho_compras.mostrar_carrinho(produtos)
                
            elif opcao == 3:
                print("Total da compra: R$", carrinho_compras.calcular_total(produtos))
                print("\n")
                pagamento = forma_pagamento(produtos)
                carrinho_compras.nota_fiscal(produtos, "Nota_Fiscal.csv", pagamento)
                return False
                
            elif opcao == 4:
                print("Compra cancelada. Saindo do sistema...")
                return False
            
        except ValueError as erro:
            print("\nErro!", str(erro))
        except Exception as erro:
            print("\nErro inesperado!", str(erro))