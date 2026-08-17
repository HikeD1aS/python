def cadastrar(acervo, titulo, autor, ano):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    }
    acervo.append(livro)


def buscar(acervo, titulo):
    for livro in acervo:
        if livro["titulo"].lower() == titulo.lower():
            return livro
    return None


def listar(acervo):
    return acervo


if __name__ == "__main__":
    teste = []

    cadastrar(teste, "Dom Casmurro", "Machado de Assis", 1899)
    cadastrar(teste, "O Cortiço", "Aluísio Azevedo", 1890)

    print(listar(teste))
    print(buscar(teste, "Dom Casmurro"))
    print(buscar(teste, "Não existe"))