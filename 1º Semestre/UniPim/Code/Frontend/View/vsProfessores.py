import customtkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image
from tkinter import messagebox
import os
# Substitua pelo caminho correto para a janela de cadastro de professores
from Frontend.Cadastro.cadProfessor import JanelaCadastroProfessor

class PaginaProfessores(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Conjunto para armazenar IDs de professores excluídos na sessão
        self.itens_excluidos = set()

        # Frame de botões
        self.frame_botoes = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(fill='x', padx=10, pady=(10, 0))

        # Ícones
        self.add_icon = self._carregar_imagem("Assets/Novo.png")
        self.edit_icon = self._carregar_imagem("Assets/Editar.png")
        self.delete_icon = self._carregar_imagem("Assets/Excluir.png")
        self.refresh_icon = self._carregar_imagem("Assets/Atualizar.png")

        # Botão Adicionar
        self.botao_adicionar = customtkinter.CTkButton(
            self.frame_botoes, text="", image=self.add_icon,
            width=40, height=40, fg_color="transparent",
            command=self.adicionar_item
        )
        self.botao_adicionar.pack(side='left', padx=5)

        # Botão Editar
        self.botao_editar = customtkinter.CTkButton(
            self.frame_botoes, text="", image=self.edit_icon,
            width=40, height=40, fg_color="transparent",
            command=self.editar_item, state="disabled"
        )
        self.botao_editar.pack(side='left', padx=5)

        # Botão Excluir
        self.botao_excluir = customtkinter.CTkButton(
            self.frame_botoes, text="", image=self.delete_icon,
            width=40, height=40, fg_color="transparent",
            command=self.excluir_item, state="disabled"
        )
        self.botao_excluir.pack(side='left', padx=5)

        # Botão Atualizar
        self.botao_atualizar = customtkinter.CTkButton(
            self.frame_botoes, text="", image=self.refresh_icon,
            width=40, height=40, fg_color="transparent",
            command=self.atualizar_grid
        )
        self.botao_atualizar.pack(side='left', padx=5)

        # Colunas da tabela
        colunas = (
            'idprofessor', 'idusuario', 'nome', 'cpf', 'data_de_nascimento',
            'status', 'email', 'telefone', 'data_de_admissao'
        )
        self.tree = ttk.Treeview(self, columns=colunas, show='headings')

        # Cabeçalhos
        self.tree.heading('idprofessor', text='ID Professor', anchor='w')
        self.tree.heading('idusuario', text='ID Usuário', anchor='w')
        self.tree.heading('nome', text='Nome', anchor='w')
        self.tree.heading('cpf', text='CPF', anchor='w')
        self.tree.heading('data_de_nascimento', text='Data de Nascimento', anchor='w')
        self.tree.heading('status', text='Status', anchor='w')
        self.tree.heading('email', text='E-mail', anchor='w')
        self.tree.heading('telefone', text='Telefone', anchor='w')
        self.tree.heading('data_de_admissao', text='Data de Admissão', anchor='w')

        # Carregar dados iniciais
        self._carregar_dados_grid()

        self.tree.pack(expand=True, fill='both', padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_item_select)

    def _carregar_imagem(self, caminho):
        """Carrega ícone da pasta Assets."""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        caminho_completo = os.path.join(script_dir, "..", caminho)
        return customtkinter.CTkImage(Image.open(caminho_completo), size=(24, 24))

    def on_item_select(self, event):
        """Habilita botões de edição e exclusão quando uma linha é selecionada."""
        if self.tree.selection():
            self.botao_editar.configure(state="normal")
            self.botao_excluir.configure(state="normal")
        else:
            self.botao_editar.configure(state="disabled")
            self.botao_excluir.configure(state="disabled")

    def adicionar_item(self):
        """Abre a janela de cadastro de professor (modo novo)."""
        # JanelaCadastroProfessor(self)
        JanelaCadastroProfessor(self)

    def editar_item(self):
        """Abre a janela de cadastro de professor (modo edição)."""
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return

        item_values = self.tree.item(selected_item_id[0], 'values')
        # Abre a janela de cadastro passando os dados do aluno para edição
        JanelaCadastroProfessor(self, professor_data=item_values)

    def excluir_item(self):
        """Remove um professor da grade com confirmação."""
        selected_item_id = self.tree.selection()
        if not selected_item_id:
            return

        confirmado = messagebox.askyesno(
            "Confirmar Exclusão",
            "Tem certeza que deseja excluir o professor selecionado?",
            icon='warning'
        )

        if confirmado:
            item_values = self.tree.item(selected_item_id[0], 'values')
            id_excluido = item_values[0]
            self.itens_excluidos.add(id_excluido)
            self.tree.delete(selected_item_id[0])
            print(f"Professor com ID {id_excluido} excluído e não será recarregado.")

    def atualizar_grid(self):
        """Atualiza os dados do grid."""
        print("Atualizando grid de professores...")
        self._carregar_dados_grid()
        print("Grid atualizado.")

    def _carregar_dados_grid(self):
        """Carrega ou recarrega os dados do grid, ignorando excluídos."""
        for i in self.tree.get_children():
            self.tree.delete(i)

        professores_exemplo = [
            ('P001', 'U100', 'Maria Silva', '123.456.789-00', '12/05/1980', 'Ativo', 'maria@escola.com', '(11)91234-5678', '10/02/2010'),
            ('P002', 'U101', 'João Souza', '987.654.321-00', '23/03/1978', 'Ativo', 'joao@escola.com', '(11)92345-6789', '05/03/2012'),
            ('P003', 'U102', 'Ana Oliveira', '741.852.963-00', '10/08/1985', 'Inativo', 'ana@escola.com', '(11)93456-7890', '20/04/2015'),
            ('P004', 'U103', 'Carlos Pereira', '852.963.741-00', '15/01/1975', 'Ativo', 'carlos@escola.com', '(11)94567-8901', '12/06/2008'),
            ('P005', 'U104', 'Fernanda Lima', '963.258.147-00', '30/09/1982', 'Ativo', 'fernanda@escola.com', '(11)95678-9012', '01/09/2013')
        ]

        for prof in professores_exemplo:
            if prof[0] not in self.itens_excluidos:
                self.tree.insert('', tk.END, values=prof)
