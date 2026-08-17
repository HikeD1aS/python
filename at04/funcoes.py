i = True
acervo = []
quantLivros = 0


def media(notas):
    return sum(notas) / len(notas)


def situacao(nota, corte=7.0):
    if nota >= corte:
        return "aprovado"
    return "recuperacao"


def min_max(notas):
    return min(notas), max(notas)


notas = [7, 9, 5]

print(media(notas))
print(situacao(8))
print(situacao(8, 8.5))

menor, maior = min_max(notas)
print(menor, maior)


def cadastrar(acervo):
    global quantLivros

    titulo = input("Qual o título do livro?\n--> ")
    autor = input("Qual o autor do livro?\n--> ")
    ano = int(input("Qual o ano de lançamento do livro? (apenas números)\n--> "))

    acervo.append({
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    })

    quantLivros += 1


def consultar(acervo):
    titulo = input("Título:\n--> ")

    encontrado = None

    for livro in acervo:
        if livro["titulo"] == titulo:
            encontrado = livro
            break

    if encontrado:
        print(
            f"\nTítulo existe, informações:\n"
            f"Autor: {encontrado['autor']}\n"
            f"Ano: {encontrado['ano']}\n"
        )
    else:
        print("\nNão está no acervo\n")


def listar(acervo):
    for livro in acervo:
        print(
            f"{livro['titulo']} ({livro['ano']}) - {livro['autor']}"
        )

    print(f"\nTotal -> {quantLivros} livros\n")


while i == True:
    pergunta = input(
        "1- Cadastrar Livro\n"
        "2- Consultar Livro\n"
        "3- Listar\n"
        "0- Sair\n"
        "--> "
    )

    if pergunta == "1":
        cadastrar(acervo)

    elif pergunta == "2":
        consultar(acervo)

    elif pergunta == "3":
        listar(acervo)

    elif pergunta == "0":
        break