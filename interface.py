import tkinter as tk
from tkinter import messagebox

import funcoes

janela = tk.Tk() #cria a janela do programa

receitas, despesas = funcoes.carregar_dados()

janela.title("Projeto 12x8") #define o que aparecerá no topo da janela

janela.geometry("600x500") #define largura e altura = 600px lar x 500 px de altura

titulo = tk.Label(
    janela,
    text="PROJETO 12X8",
    font=("Arial", 24, "bold")
)  # mantém a janela aberta e aguardando interações / #mostrar texto

titulo.pack(pady=30) #pack -> colocar elementos na janela

saldo = tk.Label(
    janela,
    text="Saldo: R$ 0,00",
    font=("Arial", 18)
)

saldo.pack(pady=20)

informacoes = tk.Label(
    janela,
    text="Últimas movimentações",
    font=("Arial", 14)
)

informacoes.pack(pady=20)

def tela_adicionar_receita():
    janela_receita = tk.Toplevel(janela)

    janela_receita.title("Adicionar Receita")
    janela_receita.geometry("400x300")

    def salvar_receita():
        descricao = entrada_descricao.get()
        valor = float(entrada_valor.get())
        data = entrada_data.get()
    
        receita = {
            "descricao": descricao,
            "valor": valor,
            "data": data
        }

        receitas.append(receita)

        funcoes.salvar_dados(receitas, despesas)
        atualizar_lista()
        atualizar_saldo()

        janela_receita.destroy()

    tk.Label(
        janela_receita,
        text="Descrição:"
    ).pack()

    entrada_descricao = tk.Entry(janela_receita)
    entrada_descricao.pack()

    tk.Label(
        janela_receita,
        text="Valor:"
    ).pack()

    entrada_valor = tk.Entry(janela_receita)
    entrada_valor.pack()

    tk.Label(
        janela_receita,
        text="Data:"
    ).pack()

    entrada_data = tk.Entry(janela_receita)
    entrada_data.pack()

    botao_salvar = tk.Button(
        janela_receita,
        text="SALVAR",
        command=salvar_receita
    )

    botao_salvar.pack(pady=20)

def tela_adicionar_despesa():
    janela_despesa = tk.Toplevel(janela)

    janela_despesa.title("Adicionar Despesa")
    janela_despesa.geometry("400x350")

    def salvar_despesa():
        descricao = entrada_descricao.get()
        valor = float(entrada_valor.get())
        categoria = entrada_categoria.get()
        data = entrada_data.get()

        despesa = {
            "descricao": descricao,
            "valor": valor,
            "categoria": categoria,
            "data": data
        }

        despesas.append(despesa)

        funcoes.salvar_dados(receitas, despesas)
        atualizar_lista()
        atualizar_saldo()

        janela_despesa.destroy()

    tk.Label(
            janela_despesa,
            text="Descrição:"
        ).pack()

    entrada_descricao = tk.Entry(janela_despesa)
    entrada_descricao.pack()

    tk.Label(
        janela_despesa,
        text="Valor:"
    ).pack()

    entrada_valor = tk.Entry(janela_despesa)
    entrada_valor.pack()

    tk.Label(
        janela_despesa,
        text="Categoria:"
    ).pack()

    entrada_categoria = tk.Entry(janela_despesa)
    entrada_categoria.pack()

    tk.Label(
        janela_despesa,
        text="Data:"
    ).pack()

    entrada_data = tk.Entry(janela_despesa)
    entrada_data.pack()

    botao_salvar = tk.Button(
        janela_despesa,
        text="SALVAR",
        command=salvar_despesa
    )

    botao_salvar.pack(pady=20)

lista_movimentacoes = tk.Listbox(
    janela,
    width=60,
    height=8
)

lista_movimentacoes.pack(pady=10)

movimentacoes = []

def atualizar_lista():
    movimentacoes.clear()

    lista_movimentacoes.delete(0, tk.END)

    for indice, receita in enumerate(receitas):
        movimentacoes.append(("receita", indice))

        lista_movimentacoes.insert(
            tk.END,
            f"Receita | {receita['descricao']} | {funcoes.formatar_moeda(receita['valor'])}"
        )

    for indice, despesa in enumerate(despesas):
        movimentacoes.append(("despesa", indice))

        lista_movimentacoes.insert(
            tk.END,
            f"Despesa | {despesa['descricao']} | {funcoes.formatar_moeda(despesa['valor'])}"
        )

atualizar_lista()

def atualizar_saldo():
    total_receitas = funcoes.calcular_total(receitas)
    total_despesas = funcoes.calcular_total(despesas)

    saldo_atual = funcoes.calcular_saldo(
        total_receitas,
        total_despesas
    )

    saldo.config(
        text=f"Saldo: {funcoes.formatar_moeda(saldo_atual)}"
    )

atualizar_lista()
atualizar_saldo()

botao_receita = tk.Button(
    janela,
    text="Adicionar Receita",
    command=tela_adicionar_receita
)

botao_receita.pack(pady=5)

botao_despesa = tk.Button(
    janela,
    text="Adicionar Despesa",
    command=tela_adicionar_despesa
)

botao_despesa.pack(pady=5)

botao_resumo = tk.Button(
    janela,
    text="Ver Resumo"
)

botao_resumo.pack(pady=5)

def editar_selecionado():
    selecionado = lista_movimentacoes.curselection()

    if not selecionado:
        messagebox.showwarning(
            "Atenção!",
            "Selecione uma movimentação para editar."
        )
        return

    indice_lista = selecionado[0]

    tipo, indice = movimentacoes[indice_lista]

    if tipo == "receita":
        item = receitas[indice]
    else:
        item = despesas[indice]

    janela_editar = tk.Toplevel(janela)

    janela_editar.title(
        "Editar Receita." if tipo == "receita" else "Editar Despesa."
    )

    janela_editar.geometry("400x300")

    tk.Label(
        janela_editar,
        text="Descricao:"
    ).pack()

    entrada_descricao = tk.Entry(janela_editar)
    entrada_descricao.pack()

    entrada_descricao.insert(
        0,
        item["descricao"]
    )

    tk.Label(
        janela_editar,
        text="Valor:"
    ).pack()

    entrada_valor = tk.Entry(janela_editar)
    entrada_valor.pack()

    entrada_valor.insert(
        0,
        str(item["valor"])
    )

    tk.Label(
        janela_editar,
        text="Data:"
    ).pack()

    entrada_data = tk.Entry(janela_editar)
    entrada_data.pack()

    entrada_data.insert(
        0,
        item["data"]
    )

    if tipo == "despesa":

        tk.Label(
            janela_editar,
            text="Categoria:"
        ).pack()

        entrada_categoria = tk.Entry(janela_editar)
        entrada_categoria.pack()

        entrada_categoria.insert(
            0,
            item["categoria"]
        )

    def salvar_edicao():
        nova_descricao = entrada_descricao.get()
        novo_valor = float(entrada_valor.get())
        nova_data = entrada_data.get()

        item["descricao"] = nova_descricao
        item["valor"] = novo_valor
        item["data"] = nova_data

        if tipo == "despesa":
            item["categoria"] = entrada_categoria.get()


        funcoes.salvar_dados(receitas, despesas)

        atualizar_lista()
        atualizar_saldo()

        janela_editar.destroy()

    botao_salvar = tk.Button(
        janela_editar,
        text="SALVAR",
        command=salvar_edicao
    )

    botao_salvar.pack(pady=20)

botao_editar = tk.Button(
    janela, 
    text="Editar",
    command=editar_selecionado
)


botao_editar.pack(pady=5)

def excluir_selecionado():
    selecionado = lista_movimentacoes.curselection()

    if not selecionado:
        messagebox.showwarning(
            "Atenção!",
            "Selecione uma movimentação para excluir."
        )
        return

    indice_lista = selecionado[0]

    tipo, indice = movimentacoes[indice_lista]

    if tipo == "receita":
        item = receitas[indice]
    else:
        item = despesas[indice]

    confirmacao = messagebox.askyesno(
        "Confirmar exclusão",
        f"Deseja excluir:\n\n{item['descricao']}?"
    )

    if not confirmacao:
        return

    if tipo == "receita":
        del receitas[indice]
    else: 
        del despesas[indice]

    funcoes.salvar_dados(receitas, despesas)

    atualizar_lista()
    atualizar_saldo()

botao_excluir = tk.Button(
    janela,
    text="Excluir",
    command=excluir_selecionado
)

botao_excluir.pack(pady=5)

janela.mainloop()