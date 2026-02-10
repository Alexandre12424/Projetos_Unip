import customtkinter
from tkinter import messagebox

class JanelaCadastroSala(customtkinter.CTkToplevel):
    def __init__(self, parent, sala_data=None):
        super().__init__(parent)
        self.parent = parent
        self.sala_data = sala_data

        # --- CONFIGURAÇÃO DA JANELA ---
        self.title("Cadastro de Sala")
        self.geometry("400x420")
        self.transient(parent)  # Mantém a janela sobre a principal
        self.grab_set()         # Torna a janela modal
        self.resizable(False, False)

        # Centraliza a janela após a criação
        self.after(10, self._center_window)

        # Determina se está em modo de edição ou criação
        self.is_edit_mode = self.sala_data is not None

        # --- WIDGETS ---
        self.frame_principal = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_principal.pack(expand=True, fill="both", padx=20, pady=20)

        # Campo Nome/Número
        self.label_nome = customtkinter.CTkLabel(self.frame_principal, text="Nome/Número:")
        self.label_nome.pack(anchor="w")
        self.entry_nome = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Ex: Sala 101")
        self.entry_nome.pack(fill="x", pady=(0, 10))

        # Campo Bloco
        self.label_bloco = customtkinter.CTkLabel(self.frame_principal, text="Bloco:")
        self.label_bloco.pack(anchor="w")
        self.entry_bloco = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Ex: Bloco A")
        self.entry_bloco.pack(fill="x", pady=(0, 10))

        # Campo Capacidade
        self.label_capacidade = customtkinter.CTkLabel(self.frame_principal, text="Capacidade:")
        self.label_capacidade.pack(anchor="w")
        self.entry_capacidade = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Ex: 40")
        self.entry_capacidade.pack(fill="x", pady=(0, 10))

        # Campo Tipo
        tipos_sala = ['Sala de Aula', 'Laboratório', 'Auditório', 'Sala de Reunião']
        self.label_tipo = customtkinter.CTkLabel(self.frame_principal, text="Tipo:")
        self.label_tipo.pack(anchor="w")
        self.combo_tipo = customtkinter.CTkComboBox(self.frame_principal, values=tipos_sala)
        self.combo_tipo.pack(fill="x", pady=(0, 10))

        # Campo Status
        status_sala = ['Disponível', 'Ocupada', 'Manutenção', 'Indisponível']
        self.label_status = customtkinter.CTkLabel(self.frame_principal, text="Status:")
        self.label_status.pack(anchor="w")
        self.combo_status = customtkinter.CTkComboBox(self.frame_principal, values=status_sala)
        self.combo_status.pack(fill="x", pady=(0, 20))

        # --- BOTÕES ---
        self.frame_botoes = customtkinter.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_botoes.pack(fill="x")

        self.botao_salvar = customtkinter.CTkButton(self.frame_botoes, text="Salvar", command=self.salvar_sala)
        self.botao_salvar.pack(side="right", padx=(10, 0))

        self.botao_cancelar = customtkinter.CTkButton(self.frame_botoes, text="Cancelar", fg_color="gray", command=self.destroy)
        self.botao_cancelar.pack(side="right")

        # Se estiver em modo de edição, preenche os campos
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
        """Preenche os campos do formulário com os dados da sala para edição."""
        # sala_data = ('idsala', 'nome', 'bloco', 'capacidade', 'tipo', 'status')
        self.entry_nome.insert(0, self.sala_data[1])
        self.entry_bloco.insert(0, self.sala_data[2])
        self.entry_capacidade.insert(0, self.sala_data[3])
        self.combo_tipo.set(self.sala_data[4])
        self.combo_status.set(self.sala_data[5])

    def salvar_sala(self):
        """Valida e salva os dados da sala."""
        nome = self.entry_nome.get().strip()
        bloco = self.entry_bloco.get().strip()
        capacidade_str = self.entry_capacidade.get().strip()
        tipo = self.combo_tipo.get()
        status = self.combo_status.get()

        # --- VALIDAÇÃO ---
        if not all([nome, bloco, capacidade_str]):
            messagebox.showerror("Erro de Validação", "Todos os campos, exceto 'Tipo' e 'Status', são obrigatórios.", parent=self)
            return

        try:
            capacidade = int(capacidade_str)
            if capacidade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro de Validação", "A capacidade deve ser um número inteiro positivo.", parent=self)
            return

        # --- LÓGICA DE SALVAMENTO ---
        if self.is_edit_mode:
            # Aqui você atualizaria os dados no banco de dados
            print(f"Editando sala ID {self.sala_data[0]}: {nome}, {bloco}, {capacidade}, {tipo}, {status}")
        else:
            # Aqui você inseriria os novos dados no banco de dados
            print(f"Adicionando nova sala: {nome}, {bloco}, {capacidade}, {tipo}, {status}")

        # Atualiza o grid na janela principal e fecha a janela de cadastro
        self.parent.atualizar_grid()
        self.destroy()