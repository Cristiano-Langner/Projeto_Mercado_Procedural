from Estoque.estoque import carregar_produtos, listar_produtos

#Função principal.
def main():
    produtos = carregar_produtos("Estoque/produtos.csv")
    
    while True:
        try:
            print("==== Mercado ====")
            print("1. Comprar produtos")
            print("2. Concluir compra")
            print("3. Sair")
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                listar_produtos(produtos)
                codigo = input("Digite o código do produto: ")
                quantidade = int(input("Digite a quantidade: "))
            elif opcao == 2:
                break
            elif opcao == 3:
                print("Saindo...")
                break
            else:
                pass
            
        except Exception as e:
            print("Ocorreu um erro:", str(e))
            
if __name__ == "__main__":
    main()