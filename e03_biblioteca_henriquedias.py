acervo = []
quantLivros = 0
i = True

while i == True:
    pergunta = input("1- Cadastrar Livro\n2- Consultar Livro\n3- Listar\n0- Sair\n--> ")
    if(pergunta == "1"):
        titulo = input("Qual o título do livro?\n-->")
        autor = input("Qual o autor do livro?\n-->")
        ano = int(input("Qual o ano de lançamento do livro? (apenas numeros)\n-->"))
        acervo.append({"titulo": titulo, "autor": autor, "ano": ano})
        quantLivros += 1

    if(pergunta == "2"):
        procurado = input("Titulo:\n-->")
        encontrado = None
        
        for livro in acervo:
            if livro["titulo"] == procurado:
                encontrado = livro
                break
        if encontrado:
            print(f"Titulo existe, informações:\nAutor: {encontrado["autor"]}\nAno: {encontrado['ano']}\n\n")
        else:
            print("Não está no acervo\n\n")
                    
                    
    if(pergunta == "3"):
        for livro in acervo:
            print(f"\n{livro["titulo"]} ({livro['ano']}) - {livro['autor']}\n")
            
        print(f"\n Total -> {quantLivros} livros")
                    
    if(pergunta == "0"):
        print("Obrigado por usar o sistema, até a proxima!")
        break
    
    else:
        print("\n -- Por favor, digite uma opção valida -- \n")
        
# ---  PERGUNTAS ---
# 1- Nada impede a criação de livros sem ano, pois não é validado.
# 2- Nada impede escrever um texto na área de ano, pois também não é validado
# 3- Em todos os lugares onde um livro é criado ou tratado