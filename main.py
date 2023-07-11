from Estoque.estoque import carregar_produtos, listar_produtos
from Carrinho.carrinho import Carrinho_compras

#Função principal.
def main():
    produtos, tamanho_estoque = carregar_produtos("Estoque/produtos.csv")
    carrinho_compras = Carrinho_compras()
    print("=================== Sejam Bem Vindos ao Mercado Jcavi ====================")
    print(f"=== No momento contamos com uma variedade de {tamanho_estoque} itens em nosso estoque ===")
    
    while True:
        try:
            print("1. Comprar produtos")
            print("2. Concluir compra")
            print("3. Sair")
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                listar_produtos(produtos)
                codigo = input("Digite o código do produto: ")
                if 1 <= int(codigo) <= tamanho_estoque:
                    quantidade = int(input("Digite a quantidade: "))
                    carrinho_compras.adicionar_produtos(produtos, codigo, quantidade)
                else:
                    raise ValueError("O produto está fora de estoque!\n")
            elif opcao == 2:
                break
            elif opcao == 3:
                print("Compra cancelada. Saindo do sistema...")
                break
            else:
                pass
            
        except Exception as e:
            print("\nErro! ", str(e))
            print("Escolha uma opção: ")
            
if __name__ == "__main__":
    main()