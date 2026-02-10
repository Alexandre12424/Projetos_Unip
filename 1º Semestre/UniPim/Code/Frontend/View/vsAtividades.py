import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image
from tkinter import messagebox
import os
from Frontend.Cadastro.cadAtividade import JanelaCadastroAtividade # Importar a janela correta para atividades

class PaginaAtividades(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Conjunto para armazenar os IDs dos itens excluídos durante a sessão
        self.itens_excluidos = set()

        self.frame_superior = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_superior.pack(fill='x', padx=10, pady=(10, 0))

        # Carregar ícones
        self.add_icon = self._carregar_imagem("Assets/Novo.png")
        self.edit_icon = self._carregar_imagem("Assets/Editar.png")
        self.delete_icon = self._carregar_imagem("Assets/Excluir.png")
        self.refresh_icon = self._carregar_imagem("Assets/Atualizar.png")
        self.sort_asc_icon = self._carregar_imagem("Assets/Asc.png", (32, 32))
        self.sort_desc_icon = self._carregar_imagem("Assets/Desc.png", (32, 32))
        
        # Botões
        self.botao_adicionar = customtkinter.CTkButton(
            self.frame_superior, text="", image=self.add_icon,
            width=40, height=40, fg_color="transparent",
            command=self.adicionar_item
        )
        self.botao_adicionar.pack(side='left', padx=5)

        self.botao_editar = customtkinter.CTkButton(
            self.frame_superior, text="", image=self.edit_icon,
            width=40, height=40, fg_color="transparent",
            command=self.editar_item, state="disabled"
        )
        self.botao_editar.pack(side='left', padx=5)

        self.botao_excluir = customtkinter.CTkButton(
            self.frame_superior, text="", image=self.delete_icon,
            width=40, height=40, fg_color="transparent",
            command=self.excluir_item, state="disabled"
        )
        self.botao_excluir.pack(side='left', padx=5)

        self.botao_atualizar = customtkinter.CTkButton(
            self.frame_superior, text="", image=self.refresh_icon,
            width=40, height=40, fg_color="transparent",
            command=self.atualizar_grid
        )
        self.botao_atualizar.pack(side='left', padx=5)

        # Dados para a tabela
        colunas = ('id', 'titulo', 'materia', 'data_entrega')
        self.tree = ttk.Treeview(self, columns=colunas, show='headings')
        self._sort_state = {} # Dicionário para guardar o estado da ordenação
        
        # Cabeçalhos com comando de ordenação
        self.tree.heading('id', text='ID', anchor='w', command=lambda: self._ordenar_coluna('id'))
        self.tree.heading('titulo', text='Título', anchor='w', command=lambda: self._ordenar_coluna('titulo'))
        self.tree.heading('materia', text='Matéria', anchor='w', command=lambda: self._ordenar_coluna('materia'))
        self.tree.heading('data_entrega', text='Data de Entrega', anchor='w', command=lambda: self._ordenar_coluna('data_entrega'))

        # Ajuste de largura das colunas (opcional)
        self.tree.column('id', width=50)
        self.tree.column('titulo', width=250)

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
        if self.tree.selection():
            self.botao_editar.configure(state="normal")
            self.botao_excluir.configure(state="normal")
        else:
            self.botao_editar.configure(state="disabled")
            self.botao_excluir.configure(state="disabled")

    def adicionar_item(self):
        # Abre a janela de cadastro sem passar dados, indicando uma nova atividade
        JanelaCadastroAtividade(self) # Chamar a janela correta para atividades

    def editar_item(self):
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return
        
        # Pega os valores da linha selecionada no grid
        item_values = self.tree.item(selected_item_id[0], 'values')
        # Abre a janela de cadastro passando os dados da atividade para edição
        JanelaCadastroAtividade(self, atividade_data=item_values)

    def excluir_item(self):
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return
        
        # Pede confirmação ao usuário antes de excluir
        confirmado = messagebox.askyesno("Confirmar Exclusão", 
                                         "Tem certeza que deseja excluir a atividade selecionada?",
                                         icon='warning')
        
        if confirmado:
            item_values = self.tree.item(selected_item_id[0], 'values')
            id_excluido = item_values[0]
            self.itens_excluidos.add(id_excluido)
            self.tree.delete(selected_item_id[0])
            print(f"Atividade com ID {id_excluido} excluída e marcada para não recarregar.")

    def atualizar_grid(self):
        print("Atualizando grid de atividades...")
        self._carregar_dados_grid()
        print("Grid atualizado.")
    
    def _carregar_dados_grid(self):
        """Limpa a grade e (re)carrega os dados, ignorando os itens excluídos."""
        # Limpa todos os itens existentes no grid
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Dados de exemplo
        atividades_exemplo = [
            ('1', 'Trabalho de Engenharia de Software', 'Engenharia de Software I', '30/11/2025'),
            ('2', 'Prova de Banco de Dados', 'Banco de Dados', '05/12/2025'),
            ('3', 'Exercícios de Lógica de Programação', 'Algoritmos', '25/11/2025'),
            ('4', 'Apresentação de Projeto Integrador', 'Projeto Integrador I', '15/12/2025'),
        ]
        # Insere as atividades na grade apenas se o ID não estiver no conjunto de excluídos
        for atividade in atividades_exemplo:
            if atividade[0] not in self.itens_excluidos:
                self.tree.insert('', tk.END, values=atividade)

    def _ordenar_coluna(self, col):
        """Ordena a treeview pela coluna especificada."""
        reverse = self._sort_state.get(col, False)
        self._sort_state[col] = not reverse

        for c in self.tree['columns']:
            self.tree.heading(c, image='')

        data = [(self.tree.set(item, col), item) for item in self.tree.get_children('')]

        try:
            data.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError:
            data.sort(key=lambda t: t[0], reverse=reverse)

        for index, (val, item) in enumerate(data):
            self.tree.move(item, '', index)

        icon = self.sort_desc_icon if reverse else self.sort_asc_icon
        self.tree.heading(col, image=icon)

        for c in self._sort_state:
            self._sort_state[c] = False if c != col else self._sort_state[c]
