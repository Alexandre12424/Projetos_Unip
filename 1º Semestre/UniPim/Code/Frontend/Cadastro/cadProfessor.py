import customtkinter
from tkinter import messagebox

class JanelaCadastroProfessor(customtkinter.CTkToplevel):
    def __init__(self, parent, professor_data=None):
        super().__init__(parent)
        self.parent = parent
        self.professor_data = professor_data

        # --- CONFIGURAÇÃO DA JANELA ---
        self.title("Cadastro de Professor")
        self.geometry("420x670")
        self.transient(parent)   # Mantém a janela sobre a principal
        self.grab_set()          # Torna a janela modal
        self.resizable(False, False)

        # Centraliza a janela após a criação
        self.after(10, self._center_window)

        # Determina se está em modo de edição
        self.is_edit_mode = self.professor_data is not None

        # --- FRAME PRINCIPAL ---
        self.frame_principal = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_principal.pack(expand=True, fill="both", padx=20, pady=20)

        # Campo ID Professor
        self.label_idprof = customtkinter.CTkLabel(self.frame_principal, text="ID Professor:")
        self.label_idprof.pack(anchor="w")
        self.entry_idprof = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Ex: P001")
        self.entry_idprof.pack(fill="x", pady=(0, 10))

        # Campo ID Usuário
        self.label_idusuario = customtkinter.CTkLabel(self.frame_principal, text="ID Usuário:")
        self.label_idusuario.pack(anchor="w")
        self.entry_idusuario = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Ex: U001")
        self.entry_idusuario.pack(fill="x", pady=(0, 10))

        # Campo Nome
        self.label_nome = customtkinter.CTkLabel(self.frame_principal, text="Nome:")
        self.label_nome.pack(anchor="w")
        self.entry_nome = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Ex: Carlos Eduardo Silva")
        self.entry_nome.pack(fill="x", pady=(0, 10))

        # Campo CPF
        self.label_cpf = customtkinter.CTkLabel(self.frame_principal, text="CPF:")
        self.label_cpf.pack(anchor="w")
        self.entry_cpf = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Ex: 123.456.789-00")
        self.entry_cpf.pack(fill="x", pady=(0, 10))

        # Campo Data de Nascimento
        self.label_data_nasc = customtkinter.CTkLabel(self.frame_principal, text="Data de Nascimento:")
        self.label_data_nasc.pack(anchor="w")
        self.entry_data_nasc = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Ex: 12/05/1980")
        self.entry_data_nasc.pack(fill="x", pady=(0, 10))

        # Campo Status (Ativo/Inativo)
        status_professor = ['Ativo', 'Inativo']
        self.label_status = customtkinter.CTkLabel(self.frame_principal, text="Status:")
        self.label_status.pack(anchor="w")
        self.combo_status = customtkinter.CTkComboBox(self.frame_principal, values=status_professor)
        self.combo_status.set("Ativo")
        self.combo_status.pack(fill="x", pady=(0, 10))

        # Campo E-mail
        self.label_email = customtkinter.CTkLabel(self.frame_principal, text="E-mail:")
        self.label_email.pack(anchor="w")
        self.entry_email = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Ex: carlos.silva@escola.com")
        self.entry_email.pack(fill="x", pady=(0, 10))

        # Campo Telefone
        self.label_telefone = customtkinter.CTkLabel(self.frame_principal, text="Telefone:")
        self.label_telefone.pack(anchor="w")
        self.entry_telefone = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Ex: (11)91234-5678")
        self.entry_telefone.pack(fill="x", pady=(0, 10))

        # Campo Data de Admissão
        self.label_data_adm = customtkinter.CTkLabel(self.frame_principal, text="Data de Admissão:")
        self.label_data_adm.pack(anchor="w")
        self.entry_data_adm = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Ex: 15/03/2010")
        self.entry_data_adm.pack(fill="x", pady=(0, 20))

        # --- BOTÕES ---
        self.frame_botoes = customtkinter.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_botoes.pack(fill="x")

        self.botao_salvar = customtkinter.CTkButton(
            self.frame_botoes, text="Salvar", command=self.salvar_professor
        )
        self.botao_salvar.pack(side="right", padx=(10, 0))

        self.botao_cancelar = customtkinter.CTkButton(
            self.frame_botoes, text="Cancelar",
            fg_color="gray",
            command=self.destroy
        )
        self.botao_cancelar.pack(side="right")

        # Preenche campos se estiver no modo de edição
        if self.is_edit_mode:
            self._preencher_campos()

    # -----------------------------------------------------

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
        """Preenche os campos com os dados do professor (modo edição)."""
        # professor_data = ('idprofessor', 'idusuario', 'nome', 'cpf', 'data_nascimento', 'status', 'email', 'telefone', 'data_admissao')
        self.entry_idprof.insert(0, self.professor_data[0])
        self.entry_idusuario.insert(0, self.professor_data[1])
        self.entry_nome.insert(0, self.professor_data[2])
        self.entry_cpf.insert(0, self.professor_data[3])
        self.entry_data_nasc.insert(0, self.professor_data[4])
        self.combo_status.set(self.professor_data[5])
        self.entry_email.insert(0, self.professor_data[6])
        self.entry_telefone.insert(0, self.professor_data[7])
        self.entry_data_adm.insert(0, self.professor_data[8])

    # -----------------------------------------------------

    def salvar_professor(self):
        """Valida e salva os dados do professor."""
        idprof = self.entry_idprof.get().strip()
        idusuario = self.entry_idusuario.get().strip()
        nome = self.entry_nome.get().strip()
        cpf = self.entry_cpf.get().strip()
        data_nasc = self.entry_data_nasc.get().strip()
        status = self.combo_status.get()
        email = self.entry_email.get().strip()
        telefone = self.entry_telefone.get().strip()
        data_adm = self.entry_data_adm.get().strip()

        # --- VALIDAÇÃO ---
        if not all([idprof, idusuario, nome, cpf, data_nasc, email]):
            messagebox.showerror("Erro de Validação", "Os campos obrigatórios devem ser preenchidos.", parent=self)
            return

        # Exemplo simples de validação de CPF (tamanho)
        if len(cpf) < 11:
            messagebox.showerror("Erro de Validação", "CPF inválido.", parent=self)
            return

        # --- LÓGICA DE SALVAMENTO ---
        if self.is_edit_mode:
            print(f"Editando professor {idprof}: {nome}, {cpf}, {email}, {status}")
        else:
            print(f"Adicionando novo professor: {nome}, {cpf}, {email}, {status}")

        # Atualiza o grid na janela principal e fecha
        self.parent.atualizar_grid()
        self.destroy()
