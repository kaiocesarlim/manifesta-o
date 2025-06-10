from operacoesbd import *
conexao = criarConexao('127.0.0.1', "root",'12345',"manifestacoes")
opcao = 1

while opcao != 7:
    print("\n1 - Listar manifestações \n2 - Listar manifestações por tipo \n3 - Adicionar nova manifestação\n4 - Total de manifestações \n5 - Pesquisar manifestação por código\n6 - Excluir manifestação pelo código.")
    opcao = int(input("Digite a opção desejada:"))

    if opcao == 1:
        consulta = "select * from manifestacoes"

        manifestacoes = (listarBancoDados(conexao, consulta))

        if len(manifestacoes) > 0:
            for item in manifestacoes:
                print("Código:", item[0], " - Título da manifestação:", item[1], " - Autor:", item[4])

        else:
            print("Não há manifestações a serem exibidas.")

    elif opcao == 2:
        tipo = int(input(
            "Digite o número equivalente ao tipo da manifestação a ser consultada:\n 1) Reclamação\n 2) Elogio\n 3) Sugestão\n"))
        consulta = 'select * from manifestacoes;'
        manifestacoes = (listarBancoDados(conexao, consulta))

        if len(manifestacoes) > 0:
            if tipo == 1:
                consulta = "select * from manifestacoes where tipo = 'Reclamação';"
                manifestacoes = (listarBancoDados(conexao, consulta))
                for item in manifestacoes:
                    print("Código:", item[0], " - Título da manifestação:", item[1], " - Descrição:", item[2],
                          "- Autor:", item[4])
            elif tipo == 2:
                consulta = "select * from manifestacoes where tipo = 'Elogio';"
                manifestacoes = (listarBancoDados(conexao, consulta))
                for item in manifestacoes:
                    print("Código:", item[0], " - Título da manifestação:", item[1], " - Descrição:", item[2],
                          "- Autor:", item[4])
            elif tipo == 3:
                consulta = "select * from manifestacoes where tipo = 'Sugestão';"
                manifestacoes = (listarBancoDados(conexao, consulta))
                for item in manifestacoes:
                    print("Código:", item[0], " - Título da manifestação:", item[1], " - Descrição:", item[2],
                          "- Autor:", item[4])


        else:
            print("Não há manifestações a serem exibidas.")

    elif opcao == 3:
        titulo = input("Digite um título: ")
        nome = input("Digite seu nome: ")
        tipo = int(
            input("Digite o número equivalente ao tipo da manifestação:\n 1) Reclamação\n 2) Elogio\n 3) Sugestão\n"))

        if tipo == 1:
            novoTipo = 'Reclamação'
            reclamacao = input("Digite a sua reclamação:")
            if len(reclamacao) <= 3:
                print("Reclamação muito curta, por favor tente novamente.")
            else:
                consulta = "insert into manifestacoes (titulo,descrição,tipo,autor) values (%s,%s,%s,%s);"
                dados = [titulo, reclamacao, novoTipo, nome]

                insert = insertNoBancoDados(conexao, consulta, dados)
                print("Manifestação recebida com sucesso. O código de sua manifestação é:", insert)

        elif tipo == 2:
            novoTipo = 'Elogio'
            reclamacao = input("Digite o seu elogio:")
            if len(reclamacao) <= 3:
                print("Reclamação muito curta, por favor tente novamente.")

            else:
                consulta = "insert into manifestacoes (titulo,descrição,tipo,autor) values (%s,%s,%s,%s);"
                dados = [titulo, reclamacao, novoTipo, nome]

                insert = insertNoBancoDados(conexao, consulta, dados)
                print("Manifestação recebida com sucesso. O código de sua manifestação é:", insert)

        elif tipo == 3:
            novoTipo = 'Sugestão'
            reclamacao = input("Digite a sua sugestão:")
            if len(reclamacao) <= 3:
                print("Reclamação muito curta, por favor tente novamente.")
            else:
                consulta = "insert into manifestacoes (titulo,descrição,tipo,autor) values (%s,%s,%s,%s);"
                dados = [titulo, reclamacao, novoTipo, nome]

                insert = insertNoBancoDados(conexao, consulta, dados)
                print("Manifestação recebida com sucesso. O código de sua manifestação é:", insert)


    elif opcao == 4:
        consulta = "select count(*) from manifestacoes"

        manifestacoes = (listarBancoDados(conexao, consulta))

        if manifestacoes[0][0] > 0:
            print("Existem", manifestacoes[0][0], "manifestações registrada(s).")

        else:
            print("Não há manifestações registradas no sistema.")

    elif opcao == 5:
        consulta = "select * from manifestacoes where codigo = %s"
        codigo = int(input("Digite o código da manifestação que você deseja pesquisar: "))
        dados = [codigo]

        pesquisa = listarBancoDados(conexao, consulta, dados)
        if len(pesquisa) > 0:
            for item in pesquisa:
                print("Código:", item[0], " - Título da manifestação:", item[1], " - Descrição:", item[2], "- Autor:",
                      item[4])
        else:
            print("Código inválido, tente novamente.")

    elif opcao == 6:
        consulta = "delete from manifestacoes where codigo = %s"
        codigo = int(input("Digite o código da manifestação que você deseja excluir: "))
        dados = [codigo]

        deletar = excluirBancoDados(conexao, consulta, dados)

        if deletar == 0:
            print("Exclusão mal sucedida, código não encontrado no sistema.")
        else:
            print("Manifestação excluída com sucesso!")

    elif opcao == 7:
        print("Muito obrigado!")

    else:
        print("Opção inválida.")

encerrarConexao(conexao)