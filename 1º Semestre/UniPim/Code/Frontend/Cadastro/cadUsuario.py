import customtkinter
from tkinter import messagebox
import re

class JanelaCadastroUsuario(customtkinter.CTkToplevel):
    def __init__(self, parent, usuario_data=None):
        super().__init__(parent)
        self.parent = parent
        self.usuario_data = usuario_data

        # --- CONFIGURAÇÃO DA JANELA ---
        self.title("Cadastro de Usuário")
        self.geometry("400x520")
        self.transient(parent)
        self.grab_set()
        self.resizable(False, False)
        
        self.after(10, self._center_window)

        self.is_edit_mode = self.usuario_data is not None

        # --- WIDGETS ---
        self.frame_principal = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_principal.pack(expand=True, fill="both", padx=20, pady=20)

        # Campo Nome
        self.label_nome = customtkinter.CTkLabel(self.frame_principal, text="Nome Completo:")
        self.label_nome.pack(anchor="w")
        self.entry_nome = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Nome do usuário")
        self.entry_nome.pack(fill="x", pady=(0, 10))

        # Campo E-mail
        self.label_email = customtkinter.CTkLabel(self.frame_principal, text="E-mail:")
        self.label_email.pack(anchor="w")
        self.entry_email = customtkinter.CTkEntry(self.frame_principal, placeholder_text="usuario@email.com")
        self.entry_email.pack(fill="x", pady=(0, 10))

        # Campo Senha
        self.label_senha = customtkinter.CTkLabel(self.frame_principal, text="Senha:")
        self.label_senha.pack(anchor="w")
        self.entry_senha = customtkinter.CTkEntry(self.frame_principal, show="*", placeholder_text="Deixe em branco para não alterar")
        self.entry_senha.pack(fill="x", pady=(0, 10))

        # Campo Confirmar Senha
        self.label_confirma_senha = customtkinter.CTkLabel(self.frame_principal, text="Confirmar Senha:")
        self.label_confirma_senha.pack(anchor="w")
        self.entry_confirma_senha = customtkinter.CTkEntry(self.frame_principal, show="*")
        self.entry_confirma_senha.pack(fill="x", pady=(0, 10))

        # Campo Tipo de Usuário
        tipos_usuario = ['ALUNO', 'PROFESSOR', 'ADM']
        self.label_tipo = customtkinter.CTkLabel(self.frame_principal, text="Tipo de Usuário:")
        self.label_tipo.pack(anchor="w")
        self.combo_tipo = customtkinter.CTkComboBox(self.frame_principal, values=tipos_usuario)
        self.combo_tipo.pack(fill="x", pady=(0, 10))

        # Campo Status
        status_usuario = ['Ativo', 'Inativo']
        self.label_status = customtkinter.CTkLabel(self.frame_principal, text="Status:")
        self.label_status.pack(anchor="w")
        self.combo_status = customtkinter.CTkComboBox(self.frame_principal, values=status_usuario)
        self.combo_status.pack(fill="x", pady=(0, 20))

        # --- BOTÕES ---
        self.frame_botoes = customtkinter.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_botoes.pack(fill="x")

        self.botao_salvar = customtkinter.CTkButton(self.frame_botoes, text="Salvar", command=self.salvar_usuario)
        self.botao_salvar.pack(side="right", padx=(10, 0))

        self.botao_cancelar = customtkinter.CTkButton(self.frame_botoes, text="Cancelar", fg_color="gray", command=self.destroy)
        self.botao_cancelar.pack(side="right")

        if self.is_edit_mode:
            self._preencher_campos()

    def _center_window(self):
        """Centraliza a janela de cadastro em relação à janela principal."""
        self.update_idletasks()
        main_window = self.parent.controller 
        parent_x = main_window.winfo_x()
        parent_y = main_window.winfo_y()
        parent_w = main_window.winfo_width()
        parent_h = main_window.winfo_height()
        
        win_w, win_h = self.winfo_width(), self.winfo_height()
        
        x = parent_x + (parent_w - win_w) // 2
        y = parent_y + (parent_h - win_h) // 2
        
        self.geometry(f"+{x}+{y}")

    def _preencher_campos(self):
        """Preenche os campos com os dados do usuário para edição."""
        # usuario_data = ('idusuario', 'nome', 'email', 'tipo_usuario', 'dt_cadastro', 'status')
        self.entry_nome.insert(0, self.usuario_data[1])
        self.entry_email.insert(0, self.usuario_data[2])
        self.combo_tipo.set(self.usuario_data[3])
        self.combo_status.set(self.usuario_data[5])

    def salvar_usuario(self):
        """Valida e salva os dados do usuário."""
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get()
        confirma_senha = self.entry_confirma_senha.get()
        tipo = self.combo_tipo.get()
        status = self.combo_status.get()

        # --- VALIDAÇÃO ---
        if not all([nome, email]):
            messagebox.showerror("Erro de Validação", "Os campos 'Nome' e 'E-mail' são obrigatórios.", parent=self)
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Erro de Validação", "O formato do e-mail é inválido.", parent=self)
            return

        if senha != confirma_senha:
            messagebox.showerror("Erro de Validação", "As senhas não coincidem.", parent=self)
            return

        # Se for um novo usuário, a senha é obrigatória
        if not self.is_edit_mode and not senha:
            messagebox.showerror("Erro de Validação", "O campo 'Senha' é obrigatório para novos usuários.", parent=self)
            return

        # --- LÓGICA DE SALVAMENTO ---
        if self.is_edit_mode:
            # Aqui você atualizaria os dados no banco de dados
            # Se a senha estiver em branco, não a atualize.
            print(f"Editando usuário ID {self.usuario_data[0]}: {nome}, {email}, Tipo: {tipo}, Status: {status}")
            if senha:
                print("Senha será atualizada.")
        else:
            # Aqui você inseriria os novos dados no banco de dados
            print(f"Adicionando novo usuário: {nome}, {email}, Tipo: {tipo}, Status: {status}")

        self.parent.atualizar_grid()
        self.destroy()