import csv

#Função para carregar os dados do estoque e armazenar em produtos_estoque[codigo,nome,valor].
def carregar_produtos(arquivo):
    produtos_estoque = {}
    with open(arquivo, "r", newline="") as f:
        reader = csv.DictReader(f, delimiter="")
        for linha in reader:
            codigo = linha("codigo")
            nome = linha("nome")
            valor = float(linha("valor"))
            produtos_estoque[codigo] = {"nome": nome, "valor": valor}
    return produtos_estoque

#Função para listar os produtos do carrinho.
def listar_carrinho(produtos):
    print("==== PRODUTOS ====")
    print("Código, Nome, Preço")
    for codigo, info in produtos.items():
        nome = info["nome"]
        valor = info["valor"]
        print(f"{codigo}, {nome}, R${valor:.2f}")