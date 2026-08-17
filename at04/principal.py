from acervo import cadastrar, buscar, listar


livros = []


while True:
    print("\n--- ACERVO ---")
    print("1 - Cadastrar livro")
    print("2 - Buscar livro")
    print("3 - Listar livros")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))

        cadastrar(livros, titulo, autor, ano)
        print("Livro cadastrado!")

    elif opcao == "2":
        titulo = input("Buscar: ")
        achado = buscar(livros, titulo)

        if achado:
            print("Titulo:", achado["titulo"])
            print("Autor:", achado["autor"])
            print("Ano:", achado["ano"])
        else:
            print("Nao esta no acervo")

    elif opcao == "3":
        todos = listar(livros)

        if len(todos) == 0:
            print("Acervo vazio")
        else:
            for livro in todos:
                print(
                    livro["titulo"],
                    "-",
                    livro["autor"],
                    "-",
                    livro["ano"]
                )

    elif opcao == "4":
        print("Programa encerrado")
        break

    else:
        print("Opcao invalida") 