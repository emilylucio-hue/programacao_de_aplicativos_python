# Cadastro de filmes

print("\ncadastro de filmes\n")

filmes = [
    "Coraline",
    "Apaixonada por você",
    "Espera de um milagre",
    "Por favor, não",
    "Socorro",

]
# Exibir todos os filmes cadastrados
print("Filmes cadastrados")
for filme in filmes:
    print(filme)

# Exibir o primeiro filme da lista
print("\nPrimeiro filme:", filmes[0])

# Exibir o último filme da lista
print("Ultimo filme:", filmes[-1])

#Adicionar um filme ao final da lista
filmes.append("Tudo vai dar certo")
print("\nDepois de adicionar Tudo vai dar certo:")
print(filmes)

#Adicionar um novo filme em uma posição especifica
filmes.insert(4,"Meu amor")
print("\nDepois de adicionar um filme na posição 5")
print(filmes)

# Remover um filme da lista
filmes.remove("Por favor, não")
print("\nDepois de remover Por favor, não:")
print(filmes)

# Alterar o nome de um dos filmes
filmes[0] = "Coraline: Meu mundo mágico"
print("Depois de alterar o nome do filme 1")
print(filmes)

# Para visualizar a quantidade de filmes cadastrados
print("\nQuantidade de filmes cadastrados", len(filmes))

# Ver se um filme está na lista de filmes disponíveis
filme_procurado = "Avatar"

if filme_procurado in filmes:
    print(f"\nO filme '{filme_procurado}' Está cadastrado.")
else:
    print(f"\nO filme '{filme_procurado}' não está cadastrado.")



