import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image
from tkinter import messagebox
import os
from Frontend.Cadastro.cadFrequencia import JanelaCadastroFrequencia

class PaginaFrequencia(customtkinter.CTkFrame):
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
        colunas = ('id', 'aluno', 'ra_aluno', 'materia', 'data', 'status')
        self.tree = ttk.Treeview(self, columns=colunas, show='headings')
        self._sort_state = {}
        
        # Cabeçalhos com comando de ordenação
        self.tree.heading('id', text='ID', anchor='w', command=lambda: self._ordenar_coluna('id'))
        self.tree.heading('aluno', text='Aluno', anchor='w', command=lambda: self._ordenar_coluna('aluno'))
        self.tree.heading('ra_aluno', text='RA', anchor='w', command=lambda: self._ordenar_coluna('ra_aluno'))
        self.tree.heading('materia', text='Matéria', anchor='w', command=lambda: self._ordenar_coluna('materia'))
        self.tree.heading('data', text='Data', anchor='w', command=lambda: self._ordenar_coluna('data'))
        self.tree.heading('status', text='Status', anchor='center', command=lambda: self._ordenar_coluna('status'))

        self.tree.column('id', width=50)
        self.tree.column('ra_aluno', width=100)
        self.tree.column('status', anchor='center')

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
        JanelaCadastroFrequencia(self)

    def editar_item(self):
        selected_item_id = self.tree.selection()
        if not selected_item_id: return
        item_values = self.tree.item(selected_item_id[0], 'values')
        JanelaCadastroFrequencia(self, frequencia_data=item_values)

    def excluir_item(self):
        selected_item_id = self.tree.selection()
        if not selected_item_id: return
        
        confirmado = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir este registro de frequência?", icon='warning')
        
        if confirmado:
            item_values = self.tree.item(selected_item_id[0], 'values')
            id_excluido = item_values[0]
            self.itens_excluidos.add(id_excluido)
            self.tree.delete(selected_item_id[0])
            print(f"Registro de frequência com ID {id_excluido} excluído.")

    def atualizar_grid(self):
        self._carregar_dados_grid()
    
    def _carregar_dados_grid(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        frequencia_exemplo = [
            ('1', 'Gabriel Liesenberg Massari', 'H7703G3', 'Engenharia de Software I', '13/11/2025', 'Presente'),
            ('2', 'João Pedro Caetano', 'R8975J5', 'Engenharia de Software I', '13/11/2025', 'Presente'),
            ('3', 'Gustavo Henrique dos S Moreira', 'H775590', 'Engenharia de Software I', '13/11/2025', 'Falta'),
            ('4', 'Gabriel Liesenberg Massari', 'H7703G3', 'Banco de Dados', '14/11/2025', 'Presente'),
        ]
        for registro in frequencia_exemplo:
            if registro[0] not in self.itens_excluidos:
                self.tree.insert('', tk.END, values=registro)

    def _ordenar_coluna(self, col):
        reverse = self._sort_state.get(col, False)
        self._sort_state[col] = not reverse

        for c in self.tree['columns']: self.tree.heading(c, image='')

        data = [(self.tree.set(item, col), item) for item in self.tree.get_children('')]
        try: data.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError: data.sort(key=lambda t: t[0], reverse=reverse)

        for index, (val, item) in enumerate(data): self.tree.move(item, '', index)

        icon = self.sort_desc_icon if reverse else self.sort_asc_icon
        self.tree.heading(col, image=icon)

        for c in self._sort_state: self._sort_state[c] = False if c != col else self._sort_state[c]