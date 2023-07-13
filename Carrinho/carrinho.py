class Carrinho_compras:
    def __init__(self):
        self.produtos_carrinho = {} # Dicionário para armazenar os produtos no carrinho de compras
        
    def adicionar_produtos(self, produtos, codigo, quantidade):
        if codigo in produtos: # Verifica se o código do produto está no estoque
            if quantidade > 0: # Verifica se a quantidade é maior que zero
                if codigo in self.produtos_carrinho: # Verifica se o produto já está no carrinho
                    self.produtos_carrinho[codigo] += quantidade # Adiciona a quantidade ao produto existente no carrinho
                else:
                    self.produtos_carrinho[codigo] = quantidade # Adiciona o produto com a quantidade ao carrinho
                print("Produto adicionado ao carrinho!")
            else:
                raise ValueError("A quantidade deve ser maior que zero!\n")
        else:
            raise ValueError("O produto está fora de estoque!\n")
        
    #Função para mostrar o carrinho de compras
    def mostrar_carrinho(self, produtos):
        print("\n=== Carrinho de compras ===")
        for codigo, quantidade in self.produtos_carrinho.items():
            nome = produtos[codigo]["nome"]
            valor = produtos[codigo]["valor"]
            print(f'Produto: {nome} - Quantidade: {quantidade} - Valor unidade: R${valor}')
        print("\n")
        
    #Função para calcular o total e apresentar os valores
    def calcular_total(self, produtos):
        total = 0
        for codigo, quantidade in self.produtos_carrinho.items():
            nome = produtos[codigo]["nome"]
            valor = produtos[codigo]["valor"]
            subtotal = valor * quantidade
            total += subtotal
            print(f"{nome} - Quantidade: {quantidade} - Subtotal: R${subtotal:.2f}")
        return total
    
    #Função para gerar a NF da compra e salvar em arquivo csv
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
                f.write(f"Desconto aplicado: R$ {round(desconto, 2)}\n")
                f.write(f"Total da compra: R$ {round(total, 2)}\n")
            else:
                f.write(f"Total da compra: R$ {round(total, 2)}\n")