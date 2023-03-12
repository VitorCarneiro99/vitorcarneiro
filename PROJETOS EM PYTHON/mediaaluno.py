while True:
    # Pergunta ao usuário o nome do aluno
    nome = input("Digite o nome do aluno: ")

    # Pergunta ao usuário as notas do aluno
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Calcula a média das notas
    media = (nota1 + nota2 + nota3) / 3

    # Verifica se a média é maior que 6 e imprime o resultado
    if media >= 5:
        print(f"O aluno {nome} está aprovado com média {media:.2f}.")
    else:
        print(f"O aluno {nome} está reprovado com média {media:.2f}.")

    # Pergunta ao usuário se ele deseja fazer uma nova verificação
    nova_verificacao = input("Deseja fazer uma nova verificação? (S/N) ")

    # Se a resposta for 'N', encerra o loop
    if nova_verificacao.upper() == "N":
        break