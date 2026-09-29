# Cadastro de funcionário
funcionario = {
"nome": "Maria",
"idade": 30,
"cargo": "Analista",
"salario": 4500,
"setor": "TI"
}

print("Nome:", funcionario["nome"])
print("Idade:", funcionario["idade"])
print("Cargo:", funcionario["cargo"])
print("Salário:", funcionario["salario"])
print("Setor:", funcionario["setor"])

funcionario["salario"] = 5000
print("Novo salário:", funcionario["salario"])

funcionario["cidade"] = "Corupá"
print("Cidade:", funcionario["cidade"])

del funcionario["idade"]

if "cargo" in funcionario:
    print("A chave cargo existe.")

for chave, valor in funcionario.items():
    print(chave, "->", valor)