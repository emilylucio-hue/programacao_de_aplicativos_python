# Controle de notas

print("Controle de notas")

notas = [ 2.0, 8.0, 7.0, 9.0,0.0]

print("Notas do aluno:", notas)
soma = sum(notas)
print("Soma dos notas:", soma)

media = soma / len(notas)
print("Media das notas do aluno:", media)

maior = max(notas)
print("Maior nota do aluno:", maior)

menor = min(notas)
print("Menor nota do aluno:", menor)

if 10 in notas:
    print("Há um 10 nas notas")
else:
    print("Não há um 10 nas notas")

    if media >= 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")