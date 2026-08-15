# Projeto 12 x 8
Tudo começou com uma conversa sobre pressão alta.
Depois de um período de muito trabalho, estudos, pouco sono e mudanças na vida, percebi que precisava encontrar equilíbrio.
Este projeto nasceu para aprender programação criando algo útil para mim.
Mais do que controlar dinheiro.
Quero construir disciplina, conhecimento e uma nova fase da minha vida.
Um passo de cada vez.

=======================================================================================================================================================================
                                                                           PROJETO 12 X 8 
=======================================================================================================================================================================

FASE 1 — FUNDAMENTOS PYTHON
━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ variáveis
✓ input / print
✓ if / elif / else
✓ while
✓ for
✓ listas
✓ dicionários
✓ funções
✓ parâmetros
✓ return
✓ módulos / import
✓ projeto financeiro CLI

        ↓

FASE 2 — PYTHON NA PRÁTICA
━━━━━━━━━━━━━━━━━━━━━━━━━━
→ tratamento de erros
→ arquivos
→ JSON
→ persistência dos dados
→ refatoração
→ organização do projeto
→ SQLite
→ banco de dados
→ SQL
→ CRUD
→ relacionamento Python + banco

        ↓

FASE 3 — BACKEND
━━━━━━━━━━━━━━━━━━━━━━━━━━
→ HTTP
→ APIs
→ Flask/FastAPI
→ endpoints
→ GET
→ POST
→ PUT/PATCH
→ DELETE
→ JSON
→ banco de dados
→ autenticação

        ↓

FASE 4 — FRONTEND
━━━━━━━━━━━━━━━━━━━━━━━━━━
→ HTML
→ CSS
→ JavaScript
→ consumir API
→ formulários
→ interface do Projeto 12X8

        ↓

FASE 5 — FULL STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━
Frontend
    ↕
API
    ↕
Backend
    ↕
Banco de dados

        ↓

FASE 6 — PROJETO PARA PORTFÓLIO
━━━━━━━━━━━━━━━━━━━━━━━━━━
Projeto 12X8 completo
Git/GitHub
README
deploy
documentação
currículo
portfólio




=====================================================================================================================================================================


def excluir_receita(receitas):
    print("Qual receita você deseja excluir?.") 

    for i, receita in enumerate(receitas):
        print(f"{i + 1} - {receita['descricao']} - {receita['valor']} - {receita['data']}")

    escolha = pedir_escolha()
    if escolha < 1 or escolha > len(receitas):
        print("Opção inválida. Por favor, escolha uma receita válida.")
        return
    indice = escolha - 1

    del receitas[indice]

    print("Receita excluída com sucesso!")

def excluir_despesa(despesas):
    print("Qual despesa você deseja excluir?") 

    for i, despesa in enumerate(despesas):
        print(f"{i + 1} - {despesa['descricao']} - {despesa['valor']} - {despesa['categoria']} - {despesa['data']}")

    escolha = pedir_escolha()
    if escolha < 1 or escolha > len(despesas):
        print("Opção inválida. Por favor, escolha uma despesa válida.")
        return
    indice = escolha - 1

    del despesas[indice]

    print("Despesa excluída com sucesso!")
