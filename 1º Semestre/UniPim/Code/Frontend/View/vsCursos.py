import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image
from tkinter import messagebox
import os
from Frontend.Cadastro.cadCursos import JanelaCadastroCurso

class PaginaCursos(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.itens_excluidos = set()

        self.frame_botoes = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(fill='x', padx=10, pady=(10, 0))

        # Carregar ícones
        self.add_icon = self._carregar_imagem("Assets/Novo.png", (24, 24))
        self.edit_icon = self._carregar_imagem("Assets/Editar.png", (24, 24))
        self.delete_icon = self._carregar_imagem("Assets/Excluir.png", (24, 24))
        self.refresh_icon = self._carregar_imagem("Assets/Atualizar.png", (24, 24))
        self.sort_asc_icon = self._carregar_imagem("Assets/Asc.png", (32, 32))
        self.sort_desc_icon = self._carregar_imagem("Assets/Desc.png", (32, 32))
        
        # Botões
        self.botao_adicionar = customtkinter.CTkButton(self.frame_botoes, text="", image=self.add_icon, width=40, height=40, fg_color="transparent", command=self.adicionar_item)
        self.botao_adicionar.pack(side='left', padx=(0, 5))

        self.botao_editar = customtkinter.CTkButton(self.frame_botoes, text="", image=self.edit_icon, width=40, height=40, fg_color="transparent", command=self.editar_item, state="disabled")
        self.botao_editar.pack(side='left', padx=5)

        self.botao_excluir = customtkinter.CTkButton(self.frame_botoes, text="", image=self.delete_icon, width=40, height=40, fg_color="transparent", command=self.excluir_item, state="disabled")
        self.botao_excluir.pack(side='left', padx=5)

        self.botao_atualizar = customtkinter.CTkButton(self.frame_botoes, text="", image=self.refresh_icon, width=40, height=40, fg_color="transparent", command=self.atualizar_grid)
        self.botao_atualizar.pack(side='left', padx=5)

        colunas = ('id', 'nome', 'coordenador', 'duracao')
        self.tree = ttk.Treeview(self, columns=colunas, show='headings')
        self._sort_state = {}
        
        self.tree.heading('id', text='ID', anchor='w', command=lambda: self._ordenar_coluna('id'))
        self.tree.heading('nome', text='Nome do Curso', anchor='w', command=lambda: self._ordenar_coluna('nome'))
        self.tree.heading('coordenador', text='Coordenador', anchor='w', command=lambda: self._ordenar_coluna('coordenador'))
        self.tree.heading('duracao', text='Duração (Semestres)', anchor='w', command=lambda: self._ordenar_coluna('duracao'))

        self._carregar_dados_grid()

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
        # Abre a janela de cadastro para um novo curso
        janela = JanelaCadastroCurso(self)
        # A janela se torna modal e a execução espera aqui
        self.wait_window(janela)
        # Após a janela ser fechada, atualiza o grid
        self.atualizar_grid()

    def editar_item(self):
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return
        
        item_values = self.tree.item(selected_item_id[0], 'values')
        # Abre a janela de cadastro com os dados do curso para edição
        janela = JanelaCadastroCurso(self, curso_data=item_values)
        self.wait_window(janela)
        # Após a janela ser fechada, atualiza o grid
        self.atualizar_grid()

    def excluir_item(self):
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return
        
        confirmado = messagebox.askyesno("Confirmar Exclusão", 
                                         "Tem certeza que deseja excluir o curso selecionado?",
                                         icon='warning')
        
        if confirmado:
            item_values = self.tree.item(selected_item_id[0], 'values')
            id_excluido = item_values[0]
            self.itens_excluidos.add(id_excluido)
            self.tree.delete(selected_item_id[0])
            print(f"Curso com ID {id_excluido} excluído e marcado para não recarregar.")

    def atualizar_grid(self):
        self._carregar_dados_grid()

    def _carregar_dados_grid(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        cursos_exemplo = [
            ('1', 'Análise e Desenvolvimento de Sistemas', 'Junior Silveira', '5'),
            ('2', 'Ciência da Computação', 'Eduardo Oliveira', '8'),
            ('3', 'Engenharia de Software', 'Cláudia Ferreira', '8')
        ]
        for curso in cursos_exemplo:
            if curso[0] not in self.itens_excluidos:
                self.tree.insert('', tk.END, values=curso)

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