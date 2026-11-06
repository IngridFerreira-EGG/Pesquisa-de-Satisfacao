entrevistados = 51

excelente = 0
bom = 0
ruim = 0

for i in range(1, entrevistados):
    print(f"--- PESQUISA DE SATISFAÇÃO ---")

    nome = input("Nome do entrevistado: ")
    idade = input("Idade do entrevistado: ")

    print("Qual a sua avaliação para o atendimento?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a sua opção (1, 2 ou 3): "))

    if opiniao == 1:
        excelente += 1

    elif opiniao == 2:
        bom += 1

    elif opiniao == 3:
        ruim += 1

    else:
        print("Opção inválida! Escolha entre 1, 2 ou 3.")

print("          RESULTADO DA PESQUISA            ")
print("Quantidade de avaliações EXCELENTE:", excelente)
print("Quantidade de avaliações BOM:", bom)
print("Quantidade de avaliações RUIM:", ruim)