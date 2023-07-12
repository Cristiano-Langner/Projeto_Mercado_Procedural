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
        
    def mostrar_carrinho(self, produtos):
        print("\n=== Carrinho de compras ===")
        for codigo, quantidade in self.produtos_carrinho.items():
            nome = produtos[codigo]["nome"]
            valor = produtos[codigo]["valor"]
            print(f'Produto: {nome} - Quantidade: {quantidade} - Valor unidade: R${valor}')
        print("\n")
        
    def calcular_total(self, produtos):
        total = 0
        for codigo, quantidade in self.produtos_carrinho.items():
            nome = produtos[codigo]["nome"]
            valor = produtos[codigo]["valor"]
            subtotal = valor * quantidade
            total += subtotal
            print(f"{nome} - Quantidade: {quantidade} - Subtotal: R${subtotal:.2f}")
        return total