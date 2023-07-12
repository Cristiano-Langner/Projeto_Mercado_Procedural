from Estoque.estoque import carregar_produtos
from Estoque.estoque import listar_produtos
from Carrinho.carrinho import Carrinho_compras

def opcoes(self):
    produtos, tamanho_estoque = carregar_produtos("Estoque/produtos.csv")
    carrinho_compras = Carrinho_compras()
    if self == 1:
        listar_produtos(produtos)
        codigo = input("Digite o código do produto: ")
        if isinstance(codigo, int):
            raise TypeError("Escolha um dos produtos disponíveis!\n")
        elif 1 <= int(codigo) <= tamanho_estoque:
            quantidade = int(input("Digite a quantidade: "))
            carrinho_compras.adicionar_produtos(produtos, codigo, quantidade)
        else:
            raise ValueError("O produto está fora de estoque!\n")
    elif self == 2:
        carrinho_compras.mostrar_carrinho()
    elif self == 3:
        print("Total da compra: R$", carrinho_compras.calcular_total(produtos))
        print("\n")
    elif self == 4:
        print("Compra cancelada. Saindo do sistema...")
        return False
    else:
        pass