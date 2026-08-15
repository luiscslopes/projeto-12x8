import json
from datetime import datetime
import os

def mostrar_menu():
    print("=================")
    print("   PROJETO 12X8")
    print("=================")
    print("")
    print("Bem vindo!")
    print("")
    print("1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("3 - Resumo Financeiro")
    print("4 - Excluir receita")
    print("5 - Excluir despesa")
    print("6 - Editar receita")
    print("7 - Editar despesa")
    print("0 - Sair")

def pausar():
    input("\nPressione Enter para continuar...")

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pedir_valor():
    while True:
        try:
            valor = float(input("Digite o valor: "))
            
            if valor <= 0:
                print("Valor inválido. Por favor, digite um número positivo.")
                continue

            return valor
            
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def pedir_inteiro():
    while True:
        try:
            escolha = int(input("Digite o número da opção: "))
            return escolha
        except ValueError:
            print("Opção inválida. Por favor, digite um número válido.")

def pedir_texto(mensagem):
    while True:
        texto = input(mensagem)

        if texto.strip() == "":
            print("Este campo não pode ficar vazio.")
            continue

        if not any(letra.isalpha() for letra in texto):
            print("Digite uma descrição válida, contendo pelo menos uma letra.")
            continue

        return texto
       
def pedir_data():
    while True:
        try:
            data = input("Digite a data (dd/mm/aaaa): ")

            datetime.strptime(data, "%d/%m/%Y")

            return data
        
        except ValueError:
            print("Data inválida. Por favor, digite uma data válida.")

def adicionar_receita():
    print("Você escolheu adicionar receita.")

    descricao, valor = pedir_dados_basicos()
    data = pedir_data()

    receita = {
            "descricao": descricao,
            "valor": valor,
            "data": data
            }
    
    return receita

def adicionar_despesa():
    print("Você escolheu adicionar despesa.")

    descricao, valor = pedir_dados_basicos()
    categoria = pedir_texto("Digite a categoria: ")
    data = pedir_data()
    
    despesa = {
            "descricao": descricao,
            "valor": valor,
            "categoria": categoria,
            "data": data
            }

    return despesa

def excluir_item(lista, mensagem_sucesso):
    if not lista:
        print("Não há itens para excluir.")
        return
    
    print("Qual item você deseja excluir?") 

    for i, item in enumerate(lista):
        print(f"{i + 1} - {item['descricao']} - {formatar_moeda(item['valor'])} - {item['data']} - ")

    escolha = pedir_inteiro()

    if escolha < 1 or escolha > len(lista):
        print("Opção inválida. Por favor, escolha um item válido.")
        return
    
    indice = escolha - 1

    print(f"\nVocê selecionou: {lista[indice]['descricao']}")
    print("Tem certeza que deseja excluir este item?")
    print("1 - Sim")
    print("2 - Não")

    confirmacao = pedir_inteiro()

    if confirmacao == 1:
        del lista[indice]
        print(mensagem_sucesso)

    elif confirmacao == 2:
        print("Exclusão cancelada.")

    else: 
        print("Opção inválida. Exclusão cancelada.")

def mostrar_resumo(receitas, despesas):
    print("==================================")
    print("      RECEITAS")
    print("==================================")

    for receita in receitas:
        print("Descrição: ", receita["descricao"])
        print("Valor: ", formatar_moeda(receita["valor"]))
        print("Data: ", receita["data"])
        print("-------------------")

    total_receitas = calcular_total(receitas)

    print("Total de receitas: ", formatar_moeda(total_receitas))

    print("==================================")
    print("      DESPESAS")
    print("==================================")
        
    for despesa in despesas:
        print("Descrição: ", despesa["descricao"])
        print("Valor: ", formatar_moeda(despesa["valor"]))
        print("Categoria: ", despesa["categoria"])
        print("Data: ", despesa["data"])
        print("-------------------")

    total_despesas = calcular_total(despesas)

    print("Total de despesas: ", formatar_moeda(total_despesas))

    print("==================================")
    print("      SALDO")
    print("==================================")
    saldo = calcular_saldo(total_receitas, total_despesas)
    print("Saldo: ", formatar_moeda(saldo))

def editar_item(lista, tipo, mensagem_sucesso):
    if not lista:
        print("Não há itens para editar.")
        return
    
    print("Qual item você deseja editar?") 

    for i, item in enumerate(lista):
        print(f"{i + 1} - {item['descricao']} - {formatar_moeda(item['valor'])} - {item['data']} - ")

    escolha = pedir_inteiro()

    if escolha < 1 or escolha > len(lista):
        print("Opção inválida. Por favor, escolha um item válido.")
        return
    
    indice = escolha - 1

    print(f"\nVocê selecionou: {lista[indice]['descricao']}")
    print(f"Valor atual: {formatar_moeda(lista[indice]['valor'])}")
    print(f"Data atual: {lista[indice]['data']}")

    print("Deseja editar este item?")
    print("1 - Sim")
    print("2 - Não")

    confirmacao = pedir_inteiro()

    if confirmacao == 2:
        print("Edição cancelada.")
        return

    if confirmacao != 1:
        print("Opção inválida. Edição Cancelada.")
        return

    print("\nDigite os novos dados:")

    descricao, valor = pedir_dados_basicos()
    data = pedir_data()

    lista[indice]["descricao"] = descricao
    lista[indice]["valor"] = valor
    lista[indice]["data"] = data

    if tipo == "despesa":
        categoria = pedir_texto("Digite a categoria: ")
        lista[indice]["categoria"] = categoria

    print(mensagem_sucesso)

    print("\nDados atualizados:")
    print(f"Descrição: {lista[indice]['descricao']}")
    print(f"Valor: {formatar_moeda(lista[indice]['valor'])}")
    print(f"Data: {lista[indice]['data']}")

    if tipo == "despesa":
        print(f"Categoria: {lista[indice]['categoria']}")

def calcular_total(lista):
    return sum(item["valor"] for item in lista)

def calcular_saldo(total_receitas, total_despesas):
    return total_receitas - total_despesas

def salvar_dados(receitas, despesas): 
    dados = {
        "receitas": receitas,
        "despesas": despesas
    }
    
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def carregar_dados():

    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return dados.get("receitas", []), dados.get("despesas", [])
    
    except (FileNotFoundError, json.JSONDecodeError):
        return [], []

def pedir_dados_basicos():
    descricao = pedir_texto("Digite a descrição: ")
    valor = pedir_valor()

    return descricao, valor