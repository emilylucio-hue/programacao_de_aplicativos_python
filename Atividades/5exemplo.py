# Lista de produtos
estoque = [
{"nome": "Notebook", "preco": 3500, "quantidade": 15},
{"nome": "Mouse", "preco": 80, "quantidade": 25},
{"nome": "Teclado", "preco": 150, "quantidade": 8},
{"nome": "Monitor", "preco": 1200, "quantidade": 5},
{"nome": "HD Externo", "preco": 400, "quantidade": 12}
]

# Exibir produtos
# for produto in estoque:
print(produto)

# Exibir nome, preço e quantidade
for produto in estoque
    print(produto["nome"], produto["preco"], produto["quantidade"])

# Quantidade total de itens
total = 0

for produto in estoque:
total = total + produto["quantidade"]

print("Total de itens:", total)

# Valor total do estoque
valor = 0


for produto in estoque:
valor = valor + (produto["preco"] * produto["quantidade"])

print("Valor total:", valor)

# Produtos com menos de 10 unidades
print("Estoque baixo:")

for produto in estoque:
    if produto["quantidade"] < 10:
print(produto["nome"])

# Verificar se o Mouse existe
for produto in estoque:
    if produto["nome"] == "Mouse":
print("Mouse cadastrado")

# Alterar quantidade do Mouse
for produto in estoque:
    if produto["nome"] == "Mouse":
produto["quantidade"] = 30

# Adicionar novo produto
estoque.append({
"nome": "Impressora",
"preco": 900,
"quantidade": 7
})

# Relatório final
print("\nRELATÓRIO FINAL")

for produto in estoque:
    print(produto)