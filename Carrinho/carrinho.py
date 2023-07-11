class Carrinho_compras:
    def __init__(self):
        self.produtos_carrinho = {}
        
    def adicionar_produtos(self, produtos, codigo, quantidade):
        if codigo in produtos:
            if quantidade > 0:
                if codigo in self.produtos_carrinho:
                    self.produtos_carrinho[codigo] += quantidade
                else:
                    self.produtos_carrinho[codigo] = quantidade
                print("Produto adicionado ao carrinho!")
            else:
                raise ValueError("A quantidade deve ser maior que zero!\n")
        else:
            raise ValueError("O produto está fora de estoque!\n")