from Estoque.estoque import carregar_produtos, listar_produtos
from Opcoes.opcoes import opcoes

#Função principal.
def main():
    produtos, tamanho_estoque = carregar_produtos("Estoque/produtos.csv")
    print("\n=================== Sejam Bem Vindos ao Mercado Jcavi ====================")
    print(f"=== No momento contamos com uma variedade de {tamanho_estoque} itens em nosso estoque ===\n")
    listar_produtos(produtos)
    continuar = True
    opcoes(continuar)
            
if __name__ == "__main__":
    main()