#Este programa em Python foi desenvolvido como parte de um projeto de programação procedural.
# Ele simula um sistema de compras em um supermercado, permitindo ao usuário adicionar produtos ao carrinho,
# calcular o valor total da compra e realizar o pagamento.
# O programa utiliza estruturas de dicionários para armazenar os produtos e seus respectivos valores,
# além de aplicar conceitos de exceções e condicionais para garantir a correta interação com o usuário.
# Após a conclusão da compra, os itens adquiridos são armazenados em um arquivo CSV,
# com um cabeçalho de identificação. O programa oferece opções de pagamento em dinheiro, débito e crédito,
# aplicando um desconto de 5% para as opções de pagamento em dinheiro ou débito.

from Estoque.estoque import carregar_produtos, listar_produtos
from Opcoes.opcoes import opcoes

#Função principal.
def main():
    produtos, tamanho_estoque = carregar_produtos("Estoque/produtos.csv") # Carrega os produtos do arquivo CSV
    print("\n=================== Sejam Bem Vindos ao Mercado Jcavi ====================")
    print(f"=== No momento contamos com uma variedade de {tamanho_estoque} itens em nosso estoque ===\n")
    listar_produtos(produtos) # Lista os produtos disponíveis no estoque
    continuar = True
    opcoes(continuar) # Exibe as opções disponíveis para o usuário
    
if __name__ == "__main__":
    main() # Chama a função principal