import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image
from tkinter import messagebox
import os
from Frontend.Cadastro.cadAluno import JanelaCadastroAluno

class PaginaAlunos(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Conjunto para armazenar os RAs dos itens excluídos durante a sessão
        self.itens_excluidos = set()

        self.frame_botoes = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(fill='x', padx=10, pady=(10, 0))

        # Carregar ícones
        self.add_icon = self._carregar_imagem("Assets/Novo.png")
        self.edit_icon = self._carregar_imagem("Assets/Editar.png")
        self.delete_icon = self._carregar_imagem("Assets/Excluir.png")
        self.refresh_icon = self._carregar_imagem("Assets/Atualizar.png")

        # Carregar ícones de ordenação (ASC/DESC)
        self.sort_asc_icon = self._carregar_imagem("Assets/Asc.png", (32, 32))
        self.sort_desc_icon = self._carregar_imagem("Assets/Desc.png", (32, 32))
        
        # Botões
        self.botao_adicionar = customtkinter.CTkButton(
            self.frame_botoes, text="", image=self.add_icon,
            width=40, height=40, fg_color="transparent",
            command=self.adicionar_item
        )
        self.botao_adicionar.pack(side='left', padx=5)

        self.botao_editar = customtkinter.CTkButton(
            self.frame_botoes, text="", image=self.edit_icon,
            width=40, height=40, fg_color="transparent",
            command=self.editar_item, state="disabled"
        )
        self.botao_editar.pack(side='left', padx=5)

        self.botao_excluir = customtkinter.CTkButton(
            self.frame_botoes, text="", image=self.delete_icon,
            width=40, height=40, fg_color="transparent",
            command=self.excluir_item, state="disabled"
        )
        self.botao_excluir.pack(side='left', padx=5)

        self.botao_atualizar = customtkinter.CTkButton(
            self.frame_botoes, text="", image=self.refresh_icon,
            width=40, height=40, fg_color="transparent",
            command=self.atualizar_grid
        )
        self.botao_atualizar.pack(side='left', padx=5)



        # Dados para a tabela
        colunas = ('ra', 'nome', 'curso', 'cpf', 'data_nascimento', 'email', 'telefone')
        self.tree = ttk.Treeview(self, columns=colunas, show='headings')
        self._sort_state = {} # Dicionário para guardar o estado da ordenação de cada coluna
        
        # Configura os cabeçalhos e o comando de ordenação para cada coluna
        self.tree.heading('ra', text='RA', anchor='w', command=lambda: self._ordenar_coluna('ra'))
        self.tree.heading('nome', text='Nome', anchor='w', command=lambda: self._ordenar_coluna('nome'))
        self.tree.heading('curso', text='Curso', anchor='w', command=lambda: self._ordenar_coluna('curso'))
        self.tree.heading('cpf', text='CPF', anchor='w', command=lambda: self._ordenar_coluna('cpf'))
        self.tree.heading('data_nascimento', text='Data de Nascimento', anchor='w', command=lambda: self._ordenar_coluna('data_nascimento'))
        self.tree.heading('email', text='E-mail', anchor='w', command=lambda: self._ordenar_coluna('email'))
        self.tree.heading('telefone', text='Telefone', anchor='w', command=lambda: self._ordenar_coluna('telefone'))

        self._carregar_dados_grid()

        self.tree.pack(expand=True, fill='both', padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_item_select)


    def _carregar_imagem(self, caminho, size=(24, 24)):
        # O diretório 'Assets' está um nível acima do diretório 'View'
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Sobe um nível para o diretório 'frontend' e depois entra em 'Assets'
        caminho_completo = os.path.join(script_dir, "..", caminho)
        return customtkinter.CTkImage(Image.open(caminho_completo), size=size)

    def on_item_select(self, event):
        # Habilita os botões se um item for selecionado, desabilita caso contrário
        if self.tree.selection():
            self.botao_editar.configure(state="normal")
            self.botao_excluir.configure(state="normal")
        else:
            self.botao_editar.configure(state="disabled")
            self.botao_excluir.configure(state="disabled")

    def adicionar_item(self):
        # Abre a janela de cadastro sem passar dados, indicando um novo aluno
        JanelaCadastroAluno(self)

    def editar_item(self):
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return
        
        # Pega os valores da linha selecionada no grid
        item_values = self.tree.item(selected_item_id[0], 'values')
        # Abre a janela de cadastro passando os dados do aluno para edição
        JanelaCadastroAluno(self, aluno_data=item_values)

    def excluir_item(self):
        print("Botão Excluir Clicado")
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return
        
        # Pede confirmação ao usuário antes de excluir
        confirmado = messagebox.askyesno("Confirmar Exclusão", 
                                         "Tem certeza que deseja excluir o aluno selecionado?",
                                         icon='warning')
        
        if confirmado:
            # Pega os valores do item antes de deletar para obter o RA
            item_values = self.tree.item(selected_item_id[0], 'values')
            ra_excluido = item_values[0]
            self.itens_excluidos.add(ra_excluido) # Adiciona o RA ao conjunto de excluídos
            self.tree.delete(selected_item_id[0])
            print(f"Aluno com RA {ra_excluido} excluído e marcado para não recarregar.")

    def atualizar_grid(self):
        print("Atualizando grid de alunos...")
        self._carregar_dados_grid()
        
        print("Grid atualizado.")
    
    def _carregar_dados_grid(self):
        """Limpa a grade e (re)carrega os dados, ignorando os itens excluídos."""
        # Limpa todos os itens existentes no grid
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        # Dados de exemplo
        alunos_exemplo = [
            ('H7703G3', 'Gabriel Liesenberg Massari', 'Análise e Des. de Sistemas', '895.676.480-85', '02/09/2004', 'gabriel@gmail.com', '(19)91234-5678'),
            ('R8975J5', 'João Pedro Caetano', 'Análise e Des. de Sistemas', '456.456.789-00', '20/08/2003', 'joao@gmail.com', '(19)98765-4321'),
            ('H775590', 'Gustavo Henrique dos S Moreira', 'Análise e Des. de Sistemas', '789.654.321-00', '10/10/2003', 'gugu@hotmail.com', '(19)91234-5678'),
            ('R951952', 'Jean Flávio de Campos', 'Análise e Des. de Sistemas', '789.456.789-00', '15/05/2003', 'jeanzao@gmail.com', '(19)98774-4321'),
            ('H7823F3', 'Ramon Guimaraes de Oliveira', 'Análise e Des. de Sistemas', '123.456.123-00', '15/05/2003', 'ramon@gmail.com', '(19)94565-4321')
        ]
        # Insere os alunos na grade apenas se o RA não estiver no conjunto de excluídos
        for aluno in alunos_exemplo:
            if aluno[0] not in self.itens_excluidos:
                self.tree.insert('', tk.END, values=aluno)

    def _ordenar_coluna(self, col):
        """Ordena a treeview pela coluna especificada."""
        # Determina a direção da ordenação (ascendente ou descendente)
        reverse = self._sort_state.get(col, False) 
        self._sort_state[col] = not reverse

        # Limpa os ícones de ordenação de todas as colunas antes de aplicar o novo
        for c in self.tree['columns']:
            self.tree.heading(c, image='')


        # Obtém todos os itens da treeview
        data = [(self.tree.set(item, col), item) for item in self.tree.get_children('')]

        # Ordena os dados
        try:
            # Tenta ordenar numericamente se possível, senão como texto
            data.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError:
            data.sort(key=lambda t: t[0], reverse=reverse)

        # Reorganiza os itens na treeview
        for index, (val, item) in enumerate(data):
            self.tree.move(item, '', index)

        # Define o ícone de ordenação na coluna clicada
        icon = self.sort_desc_icon if reverse else self.sort_asc_icon
        self.tree.heading(col, image=icon)

        # Atualiza a direção da ordenação no cabeçalho para a próxima vez
        for c in self._sort_state:
            self._sort_state[c] = False if c != col else self._sort_state[col]
