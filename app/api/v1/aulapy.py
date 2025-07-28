# Crie um conjunto vazio chamado frutas e adicione as
# seguintes frutas a ele:
# maçã,banana,uva,laranja, morango
# Em seguida, imprima o conjunto.

# Verifique se a fruta banana está presente no conjunto frutas e imprima o resultado.

# Crie um conjunto chamado frutas_vermelhas e adicione
# as seguintes frutas a ele:
# morango
# cereja
# "framboesa
# ". Em seguida, imprima o conjunto.

# frutas=set()
# frutas.add("maçã")
# frutas.add("banana")
# frutas.add("uva")
# frutas.add("laranja")
# frutas.add("morango")
# print(frutas)
# print("banana" in frutas)

# frutas_vermelhas=set()
# frutas_vermelhas.add("morango")
# frutas_vermelhas.add("cereja")
# frutas_vermelhas.add("framboesa")
# # print(frutas_vermelhas.remove('cereja'))
# print(frutas_vermelhas)

# Crie dois conjuntos, A e B, e realize a união dos dois conjuntos.

# seta={1,9,10,25,36,87,26}
# setb={2,46,28,65,39,51}
# print(seta.union(setb))

# Crie um programa que recebe dois conjuntos e exibe a interseção deles.
# conjuntoa= set()
# conjuntob= set()
# for i in range (3):
#     valorA = input(Digite o Valor que vai ficar no conjunto A:)
#     valorB = input(Digite o Valor que vai ficar no conjunto B:)
#     conjuntoa.add(valorA)
#     conjuntob.add(valorB)
# print(conjuntoa)
# print(conjuntob)


# # Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos.


# dicionarios

# Escreva um programa que EXIBA um dicionário contendo
# informações de pessoas (nome, idade) e exiba essas informações.

# dados_usuario={
#     "Nome":"Sandro",
#     "Idade":44,
#     "Faculdade":"FAAP",
#     }
# print(dados_usuario)
# for i in dados_usuario.items():
#     print (i)

# 09- Escreva um programa que percorra as chaves e valores
# de um dicionário separadamente e os exiba.

# 10- Desenvolva um programa que recebe um dicionário, uma chave e um valor como entrada e adiciona a chave e o
# valor ao dicionário, atualizando o valor se a chave já existir.

dct = {"nome":"José"}
chave = input("Digite a chave do dicionario: ")
valor = input("Digite o valor atrelado a essa chave: ")
dct[chave] = valor
print(dct)

# 11- Escreva um programa que recebe um dicionário e uma lista de chaves como entrada e verifica se 
# todas as chaves da lista existem no dicionário. A função deve
# retornar True se todas as chaves existirem e False caso contrário.
# dct = {}
# chave = input("Digite a chave do dicionario: ")
# valor = input("Digite o valor atrelado a essa chave: ")
# print(list(dct))

# 12- Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre
# opções de eleitores e conte os votos para cada opção.
# Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o
# número de votos para cada opção. O programa deve permitir que os eleitores votem, encerre a votação e exiba
# os resultados finais. Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.


# 13- Crie um dicionário que relacione nomes de alunos às suas notas em uma disciplina. Calcule a média das notas e exiba-a.


# 14- Crie um programa que receba uma lista de números e remova todas as duplicatas usando um conjunto (set). Em
# seguida, exiba a lista original e a lista sem duplicatas.


# 15- Crie um programa que realize a união de múltiplos conjuntos e exiba o conjunto resultante.


opcoes = {
    1: "Candidato A",
    2: "Candidato B",
    3: "Candidato C"
}

# Dicionário para armazenar os votos
votos = {
    "Candidato A": 0,
    "Candidato B": 0,
    "Candidato C": 0
}

print("Bem-vindo ao sistema de votação!")
print("Escolha um dos candidatos abaixo para votar:")
for numero, nome in opcoes.items():
    print(f"{numero}: {nome}")
print("Digite 0 para encerrar a votação e ver o resultado.\n")

# Loop principal de votação
while True:
    try:
        escolha = int(input("Digite o número do seu candidato: "))
        if escolha == 0:
            print("\nVotação encerrada. Resultado final:\n")
            break
        elif escolha in opcoes:
            candidato = opcoes[escolha]
            votos[candidato] += 1
            print(f"Voto registrado para {candidato}!\n")
        else:
            print("Opção inválida. Tente novamente.\n")
    except ValueError:
        print("Por favor, digite um número válido.\n")

# Exibe o resultado final
for candidato, total_votos in votos.items():
    print(f"{candidato}: {total_votos} voto(s)")