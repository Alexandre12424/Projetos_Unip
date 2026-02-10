import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image
from tkinter import messagebox
import os
from Frontend.Cadastro.cadUsuario import JanelaCadastroUsuario

class PaginaUsuarios(customtkinter.CTkFrame):
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
        colunas = ('idusuario', 'nome', 'email', 'tipo_usuario', 'dt_cadastro', 'status')
        self.tree = ttk.Treeview(self, columns=colunas, show='headings')
        
        self.tree.heading('idusuario', text='ID', anchor='w')
        self.tree.heading('nome', text='Nome', anchor='w')
        self.tree.heading('email', text='E-mail', anchor='w')
        self.tree.heading('tipo_usuario', text='Tipo de Usuário', anchor='w')
        self.tree.heading('dt_cadastro', text='Data de Cadastro', anchor='center')
        self.tree.heading('status', text='Status', anchor='w')

        # Ajustar a largura das colunas para melhor visualização
        self.tree.column('idusuario', width=50, stretch=tk.NO)
        self.tree.column('status', width=60, stretch=tk.NO, anchor='center')
        self.tree.column('tipo_usuario', width=100, anchor='center')
        
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
        # Abre a janela de cadastro sem passar dados, indicando um novo usuário
        JanelaCadastroUsuario(self)

    def editar_item(self):
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return
        
        # Pega os valores da linha selecionada no grid
        item_values = self.tree.item(selected_item_id[0], 'values')
        # Abre a janela de cadastro passando os dados do usuário para edição
        JanelaCadastroUsuario(self, usuario_data=item_values)

    def excluir_item(self):
        print("Botão Excluir Clicado")
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return
        
        # Pede confirmação ao usuário antes de excluir
        confirmado = messagebox.askyesno("Confirmar Exclusão", 
                                         "Tem certeza que deseja excluir o usuário selecionado?",
                                         icon='warning')
        
        if confirmado:
            # Pega os valores do item antes de deletar para obter o RA
            item_values = self.tree.item(selected_item_id[0], 'values')
            id_excluido = item_values[0]
            self.itens_excluidos.add(id_excluido) # Adiciona o ID ao conjunto de excluídos
            self.tree.delete(selected_item_id[0])
            print(f"Usuário com ID {id_excluido} excluído e marcado para não recarregar.")

    def atualizar_grid(self):
        print("Atualizando grid de usuários...")
        self._carregar_dados_grid()
        
        print("Grid atualizado.")
    
    def _carregar_dados_grid(self):
        """Limpa a grade e (re)carrega os dados, ignorando os itens excluídos."""
        # Limpa todos os itens existentes no grid
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        # Dados de exemplo
        usuarios_exemplo = [
            (1, 'Gabriel Massari', 'gabriel@gmail.com', 'ALUNO', '2023-10-27', 'Ativo'),
            (2, 'João Pedro Caetano', 'joao@gmail.com', 'ALUNO', '2023-10-27', 'Ativo'),
            (3, 'Admin User', 'admin@unip.com', 'ADM', '2023-10-26', 'Ativo'),
            (4, 'Professor Eduardo', 'prof.eduardo@unip.com', 'PROFESSOR', '2023-10-25', 'Ativo'),
            (5, 'Ramon Guimaraes', 'ramon@gmail.com', 'ALUNO', '2023-10-25', 'Inativo')
        ]
        # Insere os usuários na grade apenas se o ID não estiver no conjunto de excluídos
        for usuario in usuarios_exemplo:
            # O ID do usuário é o primeiro elemento (índice 0)
            if str(usuario[0]) not in self.itens_excluidos:
                self.tree.insert('', tk.END, values=usuario)
