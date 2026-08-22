# 💰 Projeto 12X8

Sistema de controle financeiro pessoal desenvolvido em **Python** como projeto prático de estudo e evolução em programação.

O projeto começou como uma aplicação executada pelo terminal e evoluiu para uma interface gráfica utilizando **Tkinter**, permitindo o gerenciamento de receitas e despesas de forma simples e organizada.

## 🎯 Objetivo

O Projeto 12X8 foi desenvolvido para colocar em prática conceitos fundamentais de programação e, ao longo do desenvolvimento, aprofundar conhecimentos em:

* Python
* Funções e módulos
* Listas e dicionários
* Validação de dados
* Manipulação de arquivos
* JSON e persistência de dados
* CRUD
* Interface gráfica com Tkinter
* Organização e refatoração de código
* Git e GitHub

## 🚀 Funcionalidades

### 💰 Controle financeiro

* Cadastro de receitas
* Cadastro de despesas
* Edição de movimentações
* Exclusão de movimentações
* Visualização das movimentações cadastradas
* Cálculo do total de receitas
* Cálculo do total de despesas
* Cálculo do saldo
* Visualização de resumo financeiro
* Identificação de maiores e menores despesas
* Organização das movimentações por data

### 🛡️ Validações

O sistema possui validações para evitar entradas inválidas, incluindo:

* Descrição vazia
* Categoria vazia
* Valores inválidos
* Valores menores ou iguais a zero
* Datas inválidas
* Seleção de movimentações antes de editar ou excluir

### 💾 Persistência de dados

As informações são armazenadas em um arquivo **JSON**, permitindo que os dados permaneçam salvos mesmo depois que o programa é encerrado.

## 🖥️ Interface

O projeto possui uma interface gráfica desenvolvida com **Tkinter**, permitindo:

* Visualização do saldo
* Visualização das movimentações
* Cadastro de receitas e despesas
* Edição de movimentações
* Exclusão de movimentações
* Visualização do resumo financeiro

## 🛠️ Tecnologias utilizadas

* **Python**
* **Tkinter**
* **JSON**
* **Git**
* **GitHub**

## 📂 Estrutura do projeto

```text
projeto-12x8/
│
├── main.py
├── funcoes.py
├── interface.py
├── dados.json
├── .gitignore
├── HISTORIA.md
└── README.md
```

### Principais arquivos

**`main.py`**
Responsável pela execução e fluxo principal da aplicação em modo terminal.

**`funcoes.py`**
Reúne funções de validação, manipulação dos dados, cálculos financeiros e persistência em JSON.

**`interface.py`**
Contém a interface gráfica desenvolvida com Tkinter.

**`dados.json`**
Arquivo utilizado para persistência dos dados financeiros.

**`HISTORIA.md`**
Documentação da evolução e das etapas de desenvolvimento do projeto.

## ▶️ Como executar

### Pré-requisito

É necessário ter o **Python** instalado no computador.

### Execução pela interface gráfica

No terminal, dentro da pasta do projeto:

```bash
python interface.py
```

### Execução pelo terminal

Também é possível executar a versão em modo CLI:

```bash
python main.py
```

## 📚 Aprendizados

Este projeto representa minha evolução prática no aprendizado de Python.

Durante o desenvolvimento, passei de exercícios e conceitos isolados para a construção de uma aplicação com persistência de dados, validações, operações CRUD, interface gráfica e versionamento utilizando Git e GitHub.

O projeto também está sendo utilizado para praticar **organização, refatoração e melhoria contínua do código**.

## 🔮 Próximos passos

O Projeto 12X8 continuará evoluindo conforme meus estudos. Entre os próximos objetivos estão:

* Melhorar a organização do código
* Aprimorar a interface
* Implementar novos filtros e formas de consulta
* Evoluir a estrutura de armazenamento dos dados
* Estudar banco de dados e integrar o projeto com SQL
* Explorar a criação de uma API
* Continuar aplicando boas práticas de desenvolvimento

## 👨‍💻 Sobre o projeto

O Projeto 12X8 é um projeto de estudo desenvolvido por **Luis Carlos**, estudante de **Análise e Desenvolvimento de Sistemas (ADS)**.

O objetivo principal é aprender programação através da construção de projetos reais, documentando a evolução e aplicando novos conhecimentos conforme os estudos avançam.

---

⭐ Este projeto está em desenvolvimento e representa parte da minha jornada de aprendizado em tecnologia.
