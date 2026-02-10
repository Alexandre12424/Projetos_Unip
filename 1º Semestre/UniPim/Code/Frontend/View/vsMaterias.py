import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image
from tkinter import messagebox
import os
from Frontend.Cadastro.cadMaterias import JanelaCadastroMateria

class PaginaMaterias(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.frame_botoes = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(fill='x', padx=10, pady=(10, 0))

        # Carregar ícones
        self.add_icon = self._carregar_imagem("Assets/Novo.png")
        self.edit_icon = self._carregar_imagem("Assets/Editar.png")
        self.delete_icon = self._carregar_imagem("Assets/Excluir.png")
        self.refresh_icon = self._carregar_imagem("Assets/Atualizar.png")
        
        # Botões
        self.botao_adicionar = customtkinter.CTkButton(self.frame_botoes, text="", image=self.add_icon, width=40, height=40, fg_color="transparent", command=self.adicionar_item)
        self.botao_adicionar.pack(side='left', padx=(0, 5))

        self.botao_editar = customtkinter.CTkButton(self.frame_botoes, text="", image=self.edit_icon, width=40, height=40, fg_color="transparent", command=self.editar_item, state="disabled")
        self.botao_editar.pack(side='left', padx=5)

        self.botao_excluir = customtkinter.CTkButton(self.frame_botoes, text="", image=self.delete_icon, width=40, height=40, fg_color="transparent", command=self.excluir_item, state="disabled")
        self.botao_excluir.pack(side='left', padx=5)

        self.botao_atualizar = customtkinter.CTkButton(self.frame_botoes, text="", image=self.refresh_icon, width=40, height=40, fg_color="transparent", command=self.atualizar_grid)
        self.botao_atualizar.pack(side='left', padx=5)

        colunas = ('id', 'nome', 'curso', 'carga_horaria')
        self.tree = ttk.Treeview(self, columns=colunas, show='headings')
        
        self.tree.heading('id', text='ID', anchor='w')
        self.tree.heading('nome', text='Nome da Matéria', anchor='w')
        self.tree.heading('curso', text='Curso Associado', anchor='w')
        self.tree.heading('carga_horaria', text='Carga Horária', anchor='w')

        # Adicionando dados de exemplo
        materias_exemplo = [
            (1, 'Banco de Dados', 'Análise e Des. de Sistemas', '80h'),
            (2, 'Engenharia de Software I', 'Análise e Des. de Sistemas', '80h'),
            (3, 'Linguagem de Programação', 'Ciência da Computação', '120h')
        ]
        for materia in materias_exemplo:
            self.tree.insert('', tk.END, values=materia)

        self.tree.pack(expand=True, fill='both', padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_item_select)

    def _carregar_imagem(self, caminho, size=(24, 24)):
        script_dir = os.path.dirname(os.path.abspath(__file__))
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
        JanelaCadastroMateria(self)

    def editar_item(self):
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return
        
        item_values = self.tree.item(selected_item_id[0], 'values')
        JanelaCadastroMateria(self, materia_data=item_values)

    def excluir_item(self):
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return
        
        confirmado = messagebox.askyesno("Confirmar Exclusão", 
                                         "Tem certeza que deseja excluir a matéria selecionada?",
                                         icon='warning')
        
        if confirmado:
            self.tree.delete(selected_item_id[0])

    def atualizar_grid(self):
        # Limpa todos os itens existentes no grid
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        materias_exemplo = [
            (1, 'Banco de Dados', 'Análise e Des. de Sistemas', '80h'),
            (2, 'Engenharia de Software I', 'Análise e Des. de Sistemas', '80h'),
            (3, 'Linguagem de Programação', 'Ciência da Computação', '120h')
        ]
        for materia in materias_exemplo:
            self.tree.insert('', tk.END, values=materia)