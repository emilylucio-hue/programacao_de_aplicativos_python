# Tupla com as informações do produto
produto = ("Notebook", "Eletrônicos", 3500.00, "NB123")

# Exibir cada informação individualmente
print("Nome do produto:", produto[0])
print("Categoria:", produto[1])
print("Preço:", produto[2])
print("Código do produto:", produto[3])

# Exibir todas as informações com repetição
print("\nInformações do produto:")
for item in produto:
    print(item)

# Quantidade de informações armazenadas
print("\nQuantidade de informações:", len(produto))

# Tentar alterar uma informação da tupla
produto[2] = 4000.00

print(produto)