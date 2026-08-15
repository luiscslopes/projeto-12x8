import funcoes

receitas, despesas = funcoes.carregar_dados()

while True:
    funcoes.limpar_tela()
    funcoes.mostrar_menu()
    
    opcao = funcoes.pedir_inteiro()

    if opcao == 1:
        receita = funcoes.adicionar_receita()        
        receitas.append(receita)
        funcoes.salvar_dados(receitas, despesas)
        funcoes.pausar()

    elif opcao == 2:
       despesa = funcoes.adicionar_despesa()
       despesas.append(despesa)
       funcoes.salvar_dados(receitas, despesas)
       funcoes.pausar()

    elif opcao == 3:
       funcoes.mostrar_resumo(receitas, despesas)
       funcoes.pausar()

    elif opcao == 4:
        funcoes.excluir_item(receitas, "Receita excluída com sucesso!")
        funcoes.salvar_dados(receitas, despesas)
        funcoes.pausar()

    elif opcao == 5:
        funcoes.excluir_item(despesas, "Despesa excluída com sucesso!")
        funcoes.salvar_dados(receitas, despesas)
        funcoes.pausar()

    elif opcao == 6:
        funcoes.editar_item(
            receitas, 
            "receita", 
            "Receita editada com sucesso!"
        )
        funcoes.salvar_dados(receitas, despesas)
        funcoes.pausar()

    elif opcao == 7:
        funcoes.editar_item(
            despesas, 
            "despesa", 
            "Despesa editada com sucesso!"
        )
        funcoes.salvar_dados(receitas, despesas)
        funcoes.pausar()

    elif opcao == 0:
        print("Até logo!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        funcoes.pausar()