import csv

#Função para carregar os dados do estoque e armazenar em produtos_estoque[codigo,nome,valor].
def carregar_produtos(arquivo):
    produtos_estoque = {}
    with open(arquivo, "r", newline="") as f:
        reader = csv.DictReader(f, delimiter=",")
        for linha in reader:
            codigo = linha["codigo"]
            nome = linha["nome"]
            valor = float(linha["valor"])
            produtos_estoque[codigo] = {"nome": nome, "valor": valor}
    tamanho_estoque = len(produtos_estoque)
    return produtos_estoque, tamanho_estoque

#Função para mostrar os produtos do carrinho.
def listar_produtos(produtos):
    print("====== PRODUTOS ======")
    print("Código, Nome, Preço")
    for codigo, info in produtos.items():
        nome = info["nome"]
        valor = info["valor"]
        print(f"{codigo}, {nome}, R${valor:.2f}")
    print("=====================")