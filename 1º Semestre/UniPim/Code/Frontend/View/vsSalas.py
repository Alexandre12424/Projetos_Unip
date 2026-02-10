import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image
from tkinter import messagebox
import os
from Frontend.Cadastro.cadSala import JanelaCadastroSala

class PaginaSalas(customtkinter.CTkFrame):
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
        colunas = ('idsala', 'nome', 'bloco', 'capacidade', 'tipo', 'status')
        self.tree = ttk.Treeview(self, columns=colunas, show='headings')
        
        self.tree.heading('idsala', text='ID', anchor='w')
        self.tree.heading('nome', text='Nome/Número', anchor='w')
        self.tree.heading('bloco', text='Bloco', anchor='center')
        self.tree.heading('capacidade', text='Capacidade', anchor='center')
        self.tree.heading('tipo', text='Tipo', anchor='w')
        self.tree.heading('status', text='Status', anchor='center')

        # Ajustar a largura das colunas para melhor visualização
        self.tree.column('idsala', width=50, stretch=tk.NO)
        self.tree.column('bloco', width=80, anchor='center')
        self.tree.column('capacidade', width=80, anchor='center')
        self.tree.column('status', width=100, anchor='center')

        self._carregar_dados_grid()

        self.tree.pack(expand=True, fill='both', padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_item_select)

    def _carregar_imagem(self, caminho):
        # O diretório 'Assets' está um nível acima do diretório 'View'
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Sobe um nível para o diretório 'frontend' e depois entra em 'Assets'
        caminho_completo = os.path.join(script_dir, "..", caminho)
        return customtkinter.CTkImage(Image.open(caminho_completo), size=(24, 24))

    def on_item_select(self, event):
        # Habilita os botões se um item for selecionado, desabilita caso contrário
        if self.tree.selection():
            self.botao_editar.configure(state="normal")
            self.botao_excluir.configure(state="normal")
        else:
            self.botao_editar.configure(state="disabled")
            self.botao_excluir.configure(state="disabled")

    def adicionar_item(self):
        # Abre a janela de cadastro sem passar dados, indicando uma nova sala
        JanelaCadastroSala(self)

    def editar_item(self):
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return
        
        # Pega os valores da linha selecionada no grid
        item_values = self.tree.item(selected_item_id[0], 'values')
        # Abre a janela de cadastro passando os dados da sala para edição
        JanelaCadastroSala(self, sala_data=item_values)

    def excluir_item(self):
        print("Botão Excluir Clicado")
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return
        
        # Pede confirmação ao usuário antes de excluir
        confirmado = messagebox.askyesno("Confirmar Exclusão", 
                                         "Tem certeza que deseja excluir a sala selecionada?",
                                         icon='warning')
        
        if confirmado:
            # Pega os valores do item antes de deletar para obter o ID
            item_values = self.tree.item(selected_item_id[0], 'values')
            id_excluido = item_values[0]
            self.itens_excluidos.add(id_excluido) # Adiciona o ID ao conjunto de excluídos
            self.tree.delete(selected_item_id[0])
            print(f"Sala com ID {id_excluido} excluída e marcada para não recarregar.")

    def atualizar_grid(self):
        print("Atualizando grid de salas...")
        self._carregar_dados_grid()
        
        print("Grid atualizado.")
    
    def _carregar_dados_grid(self):
        """Limpa a grade e (re)carrega os dados, ignorando os itens excluídos."""
        # Limpa todos os itens existentes no grid
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        # Dados de exemplo
        salas_exemplo = [
            (1, 'Sala 101', 'Bloco A', 40, 'Sala de Aula', 'Disponível'),
            (2, 'Lab. Info I', 'Bloco B', 30, 'Laboratório', 'Ocupada'),
            (3, 'Auditório Principal', 'Bloco C', 150, 'Auditório', 'Disponível'),
            (4, 'Sala 205', 'Bloco A', 40, 'Sala de Aula', 'Manutenção'),
            (5, 'Lab. Redes', 'Bloco B', 25, 'Laboratório', 'Disponível')
        ]
        # Insere as salas na grade apenas se o ID não estiver no conjunto de excluídos
        for sala in salas_exemplo:
            if str(sala[0]) not in self.itens_excluidos:
                self.tree.insert('', tk.END, values=sala)
