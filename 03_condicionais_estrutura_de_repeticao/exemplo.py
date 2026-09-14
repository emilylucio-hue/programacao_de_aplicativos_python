# 1. Estruturas condicionais
nota = 6

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Aprovado")
else:
    print("Reprovado")

# 2. Condições com operadores lógicos
#and -> todas as condições devem ser verdadeiras.
#or -> pelo menos uma condição deve ser verdadeira.
#not -> inverte o resultado.

idade = 20
ingresso = True

if idade >= 18 and ingresso:
    print("Entrada permitida.")
else:
    print("Entrada não permitida.")

# 3. Estrutura de repetição

contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1

# 4. Estrutura  de repetição for
for numero in range(1, 6):
    print(numero)

    # 5. Percorrendo uma Lista
nomes = ["Ana","Carlos","João","Maria"]

for nome in nomes:
     print(nome)

# 6. Break
# O Break interrompe completamente a repetição
# O Pass nao executa nenhuma ação
# O continue interrompe apenas a repetiçao atual

for numero in range(1, 11):
   if numero == 7:
    #break
    #pass
    continue

print(numero)

# 7. Condição dentro de repetição
for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")

