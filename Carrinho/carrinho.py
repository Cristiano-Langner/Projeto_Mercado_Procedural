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
    
    def nota_fiscal(self, produtos, arquivo, pagamento):
        total = 0
        with open(arquivo, 'w') as f:
            f.write("Nome, Quantidade, Subtotal\n")
            for codigo, quantidade in self.produtos_carrinho.items():
                nome = produtos[codigo]["nome"]
                valor = produtos[codigo]["valor"]
                subtotal = valor * quantidade
                total += subtotal
                f.write(f"{nome} - Quantidade: {quantidade} - Subtotal: R${subtotal:.2f}\n")
            if pagamento == 1 or pagamento == 3:
                desconto = total * 0.05
                total = total * (1-0.05)
                f.write(f"Desconto aplicado: R$ {desconto}\n")
                f.write(f"Total da compra: R$ {total}\n")
            else:
                f.write(f"Total da compra: R$ {total}\n")