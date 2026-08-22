import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

import funcoes

# ==================================================================================
# CONFIGURAÇÃO INICIAL
# ==================================================================================

janela = tk.Tk()  # cria a janela do programa

receitas, despesas = funcoes.carregar_dados()

janela.title("Projeto 12x8")  # define o que aparecerá no topo da janela

janela.geometry("600x500")  # define largura e altura = 600px lar x 500 px de altura

janela.minsize(600, 500)

# =================================================================================
# CONFIGURAÇÃO VISUAL
# =================================================================================

estilo = ttk.Style()
estilo.configure(
    "Treeview",
    rowheight=28
)

estilo.configure(
    "Treeview.Heading",
    font=("Arial", 10, "bold")
)

frame_cabecalho = tk.Frame(
    janela,
    bd=1,
    relief="solid",
    padx=10,
    pady=10
)

frame_cabecalho.pack(
    fill=tk.X,
    pady=10
)

titulo = tk.Label(
    frame_cabecalho,
    text="PROJETO 12X8",
    font=("Arial", 26, "bold")
)  # mantém a janela aberta e aguardando interações / #mostrar texto

titulo.pack(pady=30)  # pack -> colocar elementos na janela

subtitulo = tk.Label(
    frame_cabecalho,
    text="Controle financeiro pessoal",
    font=("Arial", 12)
)

subtitulo.pack(pady=(0, 10))

saldo = tk.Label(
    frame_cabecalho,
    text="Saldo: R$ 0,00",
    font=("Arial", 20, "bold")
)

saldo.pack(pady=20)

informacoes = tk.Label(
    janela,
    text="Últimas movimentações",
    font=("Arial", 16, "bold")
)

informacoes.pack(
    pady=(10, 5)
)

# ===================================================================================
#  VALIDAÇÕES
# ===================================================================================

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validar_valor(valor_texto):
    try:
        valor = float(valor_texto)
    except ValueError:
        return None

    return valor if valor > 0 else None

def validar_descricao(descricao):
    return bool(descricao.strip())

def validar_categoria(categoria):
    return bool(categoria.strip())

# ================================================================================
# ADIÇÃO DE MOVIMENTAÇÃO
# ================================================================================

def tela_adicionar_receita():
    janela_receita = tk.Toplevel(janela)

    janela_receita.title("Adicionar Receita")
    janela_receita.geometry("400x300")

    def salvar_receita():
        descricao = entrada_descricao.get().strip()
        valor_texto = entrada_valor.get()
        data = entrada_data.get()

        if not validar_data(data):
            messagebox.showerror(
                "Data inválida",
                "Digite uma data válida no formato DD/MM/AAAA."
            )
            return

        if not validar_descricao(descricao):
            messagebox.showerror(
                "Descrição inválida",
                "A descrição não pode ficar vazia."
            )
            return

        valor = validar_valor(valor_texto)

        if valor is None:
            messagebox.showerror(
                "Valor inválido",
                "Digite um valor numérico maior que zero."
            )
            return

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

    entrada_descricao = tk.Entry(janela_receita, width=35)
    entrada_descricao.pack(pady=5)

    tk.Label(
        janela_receita,
        text="Valor:"
    ).pack()

    entrada_valor = tk.Entry(janela_receita, width=35)
    entrada_valor.pack(pady=5)

    tk.Label(
        janela_receita,
        text="Data:"
    ).pack()

    entrada_data = tk.Entry(janela_receita, width=35)
    entrada_data.pack(pady=5)

    botao_salvar = tk.Button(
        janela_receita,
        text="SALVAR",
        command=salvar_receita,
        font=("Arial", 10, "bold"),
        padx=10,
        pady=5
    )

    botao_salvar.pack(pady=20)

def tela_adicionar_despesa():
    janela_despesa = tk.Toplevel(janela)

    janela_despesa.title("Adicionar Despesa")
    janela_despesa.geometry("400x350")

    def salvar_despesa():
        descricao = entrada_descricao.get().strip()
        valor_texto = entrada_valor.get()
        categoria = entrada_categoria.get().strip()
        data = entrada_data.get()

        if not validar_data(data):
            messagebox.showerror(
                "Data inválida",
                "Digite uma data válida no formato DD/MM/AAAA."
            )
            return

        if not validar_descricao(descricao):
            messagebox.showerror(
                "Descrição inválida",
                "A descrição não pode ficar vazia."
            )
            return

        if not validar_categoria(categoria):
            messagebox.showerror(
                "Categoria inválida",
                "A categoria não pode ficar vazia."
            )
            return

        valor = validar_valor(valor_texto)

        if valor is None:
            messagebox.showerror(
                "Valor inválido",
                "Digite um valor numérico maior que zero."
            )
            return

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

    entrada_descricao = tk.Entry(janela_despesa, width=35)
    entrada_descricao.pack(pady=5)

    tk.Label(
        janela_despesa,
        text="Valor:"
    ).pack()

    entrada_valor = tk.Entry(janela_despesa, width=35)
    entrada_valor.pack(pady=5)

    tk.Label(
        janela_despesa,
        text="Categoria:"
    ).pack()

    entrada_categoria = tk.Entry(janela_despesa, width=35)
    entrada_categoria.pack(pady=5)

    tk.Label(
        janela_despesa,
        text="Data:"
    ).pack()

    entrada_data = tk.Entry(janela_despesa, width=35)
    entrada_data.pack(pady=5)

    botao_salvar = tk.Button(
        janela_despesa,
        text="SALVAR",
        command=salvar_despesa,
        font=("Arial", 10, "bold"),
        padx=10,
        pady=5
    )

    botao_salvar.pack(pady=20)

# ================================================================================
# TABELA DE MOVIMENTAÇÕES
# ================================================================================

frame_tabela = tk.Frame(janela)

frame_tabela.pack(
    pady=10,
    padx=20,
    fill=tk.BOTH,
    expand=True
)

frame_tabela.columnconfigure(
    0,
    weight=1
)

frame_tabela.rowconfigure(
    0,
    weight=1
)

tabela_movimentacoes = ttk.Treeview(
    frame_tabela,
    columns=("tipo", "descricao", "valor", "data"),
    show="headings",
    height=8
)

tabela_movimentacoes.heading(
    "tipo",
    text="Tipo"
)

tabela_movimentacoes.heading(
    "descricao",
    text="Descrição"
)

tabela_movimentacoes.heading(
    "valor",
    text="Valor"
)

tabela_movimentacoes.heading(
    "data",
    text="Data"
)

tabela_movimentacoes.column(
    "tipo",
    width=100,
    anchor="center"
)

tabela_movimentacoes.column(
    "descricao",
    width=180
)

tabela_movimentacoes.column(
    "valor",
    width=120,
    anchor="e"
)

tabela_movimentacoes.column(
    "data",
    width=100,
    anchor="center"
)

scrollbar = ttk.Scrollbar(
    frame_tabela,
    orient=tk.VERTICAL,
    command=tabela_movimentacoes.yview
)

tabela_movimentacoes.configure(
    yscrollcommand=scrollbar.set
)

tabela_movimentacoes.grid(
    row=0,
    column=0,
    sticky="nsew"
)

scrollbar.grid(
    row=0,
    column=1,
    sticky="ns"
)

movimentacoes = []

# ================================================================================
# MOVIMENTAÇÕES
# ================================================================================

def obter_movimentacoes_ordenadas():
    lista_movimentacoes = []

    for indice, receita in enumerate(receitas):
        lista_movimentacoes.append(("Receita", indice, receita))

    for indice, despesa in enumerate(despesas):
        lista_movimentacoes.append(("Despesa", indice, despesa))

    lista_movimentacoes.sort(
        key=lambda movimentacao: datetime.strptime(
            movimentacao[2]["data"],
            "%d/%m/%Y"
        )
    )

    return lista_movimentacoes

def atualizar_lista():

    movimentacoes.clear()

    for item in tabela_movimentacoes.get_children():
        tabela_movimentacoes.delete(item)

    movimentacoes_ordenadas = obter_movimentacoes_ordenadas()

    for tipo, indice, movimentacao in movimentacoes_ordenadas:

        if tipo == "Receita":
            movimentacoes.append(("receita", indice))

        else:
            movimentacoes.append(("despesa", indice))

        tabela_movimentacoes.insert(
            "",
            tk.END,
            values=(
                tipo,
                movimentacao["descricao"],
                funcoes.formatar_moeda(movimentacao["valor"]),
                movimentacao["data"]
            )
        )

def atualizar_saldo():
    total_receitas = funcoes.calcular_total(receitas)
    total_despesas = funcoes.calcular_total(despesas)

    saldo_atual = funcoes.calcular_saldo(
        total_receitas,
        total_despesas
    )

    saldo_formatado = funcoes.formatar_moeda(saldo_atual)

    saldo.config(
        text=f"Saldo: {saldo_formatado}"
    )

# ================================================================================
# RESUMO FINANCEIRO
# ================================================================================

def mostrar_resumo():
    total_receitas = funcoes.calcular_total(receitas)
    total_despesas = funcoes.calcular_total(despesas)

    saldo_atual = funcoes.calcular_saldo(
        total_receitas,
        total_despesas
    )

    if despesas:
        maior_despesa = max(
            despesas,
            key=lambda despesa: despesa["valor"]
        )
        menor_despesa = min(
            despesas,
            key=lambda despesa: despesa["valor"]
        )
    else:
        maior_despesa = None
        menor_despesa = None

    totais_categorias = {}

    for despesa in despesas:
        categoria = despesa["categoria"]

        if categoria not in totais_categorias:
            totais_categorias[categoria] = 0

        totais_categorias[categoria] += despesa["valor"]

    # ================================================================================
    # JANELA
    # ================================================================================

    janela_resumo = tk.Toplevel(janela)

    janela_resumo.title("Resumo Financeiro")
    janela_resumo.geometry("520x550")
    janela_resumo.resizable(False, False)

    # ================================================================================
    # TÍTULO
    # ================================================================================

    tk.Label(
        janela_resumo,
        text="RESUMO FINANCEIRO",
        font=("Arial", 22, "bold")
    ).pack(pady=(25, 20))

    # ================================================================================
    # RESUMO DOS VALORES
    # ================================================================================

    quadro_valores = tk.Frame(janela_resumo)
    quadro_valores.pack(fill="x", padx=40)

    tk.Label(
        quadro_valores,
        text="Total de receitas",
        font=("Arial", 12)
    ).pack(pady=(5, 0))

    tk.Label(
        quadro_valores,
        text=funcoes.formatar_moeda(total_receitas),
        font=("Arial", 16, "bold")
    ).pack(pady=(0, 10))

    tk.Label(
        quadro_valores,
        text="Total de despesas",
        font=("Arial", 12)
    ).pack(pady=(5, 0))

    tk.Label(
        quadro_valores,
        text=funcoes.formatar_moeda(total_despesas),
        font=("Arial", 16, "bold")
    ).pack(pady=(0, 10))

    tk.Label(
        quadro_valores,
        text="Saldo",
        font=("Arial", 12)
    ).pack(pady=(5, 0))

    tk.Label(
        quadro_valores,
        text=funcoes.formatar_moeda(saldo_atual),
        font=("Arial", 18, "bold")
    ).pack(pady=(0, 15))

    # ================================================================================
    # SEPARADOR
    # ================================================================================
    tk.Frame(
        janela_resumo,
        height=2
    ).pack(fill="x", padx=40, pady=10)

    # ================================================================================
    # MAIOR E MENOR DESPESA
    # ================================================================================

    tk.Label(
        janela_resumo,
        text="PRINCIPAIS DESPESAS",
        font=("Arial", 15, "bold")
    ).pack(pady=(5, 10))

    if despesas:
        tk.Label(
            janela_resumo,
            text=(
                f"Maior despesa: {maior_despesa['descricao']} - "
                f"{funcoes.formatar_moeda(maior_despesa['valor'])}"
            ),
            font=("Arial", 12)
        ).pack(pady=3)

        tk.Label(
            janela_resumo,
            text=(
                f"Menor despesa: {menor_despesa['descricao']} - "
                f"{funcoes.formatar_moeda(menor_despesa['valor'])}"
            ),
            font=("Arial", 12)
        ).pack(pady=3)

    else:
        tk.Label(
            janela_resumo,
            text="Nenhuma despesa cadastrada.",
            font=("Arial", 12)
        ).pack(pady=5)

    # ================================================================================
    # SEPARADOR
    # ================================================================================

    tk.Frame(
        janela_resumo,
        height=2
    ).pack(fill="x", padx=40, pady=15)

    # ================================================================================
    # CATEGORIAS
    # ================================================================================

    tk.Label(
        janela_resumo,
        text="DESPESAS POR CATEGORIA",
        font=("Arial", 15, "bold")
    ).pack(pady=(0, 10))

    if totais_categorias:
        for categoria, total in totais_categorias.items():
            tk.Label(
                janela_resumo,
                text=f"{categoria}: {funcoes.formatar_moeda(total)}",
                font=("Arial", 12)
            ).pack(pady=2)

    else:
        tk.Label(
            janela_resumo,
            text="Nenhuma despesa cadastrada.",
            font=("Arial", 12)
        ).pack(pady=5)

atualizar_lista()
atualizar_saldo()

# ================================================================================
# BOTÕES E AÇÕES
# ================================================================================

frame_adicionar = tk.Frame(janela)

frame_adicionar.pack(
    pady=15,
    fill=tk.X
)

frame_acoes = tk.Frame(janela)

frame_acoes.pack(
    pady=15,
    fill=tk.X
)

frame_botoes_adicionar = tk.Frame(frame_adicionar)

frame_botoes_adicionar.pack()

frame_botoes_acoes = tk.Frame(frame_acoes)

frame_botoes_acoes.pack()

botao_receita = tk.Button(
    frame_botoes_adicionar,
    text="Adicionar Receita",
    command=tela_adicionar_receita,
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
)

botao_receita.pack(
    side=tk.LEFT,
    padx=10
)

botao_despesa = tk.Button(
    frame_botoes_adicionar,
    text="Adicionar Despesa",
    command=tela_adicionar_despesa,
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
)

botao_despesa.pack(
    side=tk.LEFT,
    padx=10
)

botao_resumo = tk.Button(
    frame_botoes_acoes,
    text="Ver Resumo",
    command=mostrar_resumo,
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
)

botao_resumo.pack(
    side=tk.LEFT,
    padx=10
)

# =================================================================================
# AÇÕES DE MOVIMENTAÇÕES
# =================================================================================

def obter_movimentacao_selecionada():
    selecionado = tabela_movimentacoes.selection()

    if not selecionado:
        return None

    id_selecionado = selecionado[0]

    indice_lista = tabela_movimentacoes.index(
        id_selecionado
    )

    return movimentacoes[indice_lista]

def obter_dados_movimentacao(selecionado):

    tipo, indice = selecionado

    if tipo == "receita":
        movimentacao = receitas[indice]
    else:
        movimentacao = despesas[indice]

    return tipo, indice, movimentacao

def editar_selecionado():
    selecionado = obter_movimentacao_selecionada()

    if selecionado is None:
        messagebox.showwarning(
            "Atenção!",
            "Selecione uma movimentação para editar."
        )
        return

    tipo, indice, movimentacao = obter_dados_movimentacao(selecionado)

    janela_editar = tk.Toplevel(janela)

    janela_editar.title(
        "Editar Receita" if tipo == "receita" else "Editar Despesa"
    )

    janela_editar.geometry("400x300")

    tk.Label(
        janela_editar,
        text="Descrição:"
    ).pack()

    entrada_descricao = tk.Entry(janela_editar, width=35)
    entrada_descricao.pack(pady=5)

    entrada_descricao.insert(
        0,
        movimentacao["descricao"]
    )

    tk.Label(
        janela_editar,
        text="Valor:"
    ).pack()

    entrada_valor = tk.Entry(janela_editar, width=35)
    entrada_valor.pack(pady=5)

    entrada_valor.insert(
        0,
        str(movimentacao["valor"])
    )

    tk.Label(
        janela_editar,
        text="Data:"
    ).pack()

    entrada_data = tk.Entry(janela_editar, width=35)
    entrada_data.pack(pady=5)

    entrada_data.insert(
        0,
        movimentacao["data"]
    )

    if tipo == "despesa":

        tk.Label(
            janela_editar,
            text="Categoria:"
        ).pack()

        entrada_categoria = tk.Entry(janela_editar, width=35)
        entrada_categoria.pack(pady=5)

        entrada_categoria.insert(
            0,
            movimentacao["categoria"]
        )

    def salvar_edicao():
        nova_descricao = entrada_descricao.get().strip()
        novo_valor = entrada_valor.get()
        nova_data = entrada_data.get()

        if not validar_data(nova_data):
            messagebox.showerror(
                "Data inválida",
                "Digite uma data válida no formato DD/MM/AAAA."
            )
            return

        if not validar_descricao(nova_descricao):
            messagebox.showerror(
                "Descrição inválida",
                "A descrição não pode ficar vazia."
            )
            return

        valor = validar_valor(novo_valor)

        if valor is None:
            messagebox.showerror(
                "Valor inválido",
                "Digite um valor numérico maior que zero."
            )
            return

        if tipo == "despesa":
            nova_categoria = entrada_categoria.get().strip()

            if not validar_categoria(nova_categoria):
                messagebox.showerror(
                    "Categoria inválida",
                    "A categoria não pode ficar vazia."
                )
                return

        movimentacao["descricao"] = nova_descricao
        movimentacao["valor"] = valor
        movimentacao["data"] = nova_data

        if tipo == "despesa":
            movimentacao["categoria"] = nova_categoria

        funcoes.salvar_dados(receitas, despesas)

        atualizar_lista()
        atualizar_saldo()

        janela_editar.destroy()

    botao_salvar = tk.Button(
        janela_editar,
        text="SALVAR",
        command=salvar_edicao,
        font=("Arial", 10, "bold"),
        padx=10,
        pady=5
    )

    botao_salvar.pack(pady=20)

botao_editar = tk.Button(
    frame_botoes_acoes,
    text="Editar",
    command=editar_selecionado,
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
)

botao_editar.pack(
    side=tk.LEFT,
    padx=10
)

# =================================================================================
# EXCLUSÃO
# =================================================================================

def excluir_selecionado():
    selecionado = obter_movimentacao_selecionada()

    if selecionado is None:
        messagebox.showwarning(
            "Atenção!",
            "Selecione uma movimentação para excluir."
        )
        return

    tipo, indice, movimentacao = obter_dados_movimentacao(selecionado)

    confirmacao = messagebox.askyesno(
        "Confirmar exclusão",
        f"Deseja excluir:\n\n{movimentacao['descricao']}?"
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
    frame_botoes_acoes,
    text="Excluir",
    command=excluir_selecionado,
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
)

botao_excluir.pack(
    side=tk.LEFT,
    padx=10
)

janela.mainloop()