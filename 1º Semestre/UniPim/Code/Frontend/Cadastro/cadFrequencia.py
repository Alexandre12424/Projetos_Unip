import customtkinter
from tkinter import messagebox

class JanelaCadastroFrequencia(customtkinter.CTkToplevel):
    def __init__(self, parent, frequencia_data=None):
        super().__init__(parent)
        self.parent = parent
        self.frequencia_data = frequencia_data

        # --- CONFIGURAÇÃO DA JANELA ---
        self.title("Registrar Frequência" if frequencia_data is None else "Editar Frequência")
        self.geometry("400x380")
        self.transient(parent)
        self.grab_set()
        self.resizable(False, False)
        
        self.after(10, self._center_window)

        self.is_edit_mode = self.frequencia_data is not None

        # --- WIDGETS ---
        self.frame_principal = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_principal.pack(expand=True, fill="both", padx=20, pady=20)

        # Campo Aluno (ComboBox)
        alunos_disponiveis = ['Gabriel Liesenberg Massari', 'João Pedro Caetano', 'Gustavo Henrique dos S Moreira', 'Jean Flávio de Campos', 'Ramon Guimaraes de Oliveira']
        self.label_aluno = customtkinter.CTkLabel(self.frame_principal, text="Aluno:")
        self.label_aluno.pack(anchor="w")
        self.combo_aluno = customtkinter.CTkComboBox(self.frame_principal, values=alunos_disponiveis)
        self.combo_aluno.pack(fill="x", pady=(0, 10))

        # Campo Matéria (ComboBox)
        materias_disponiveis = ['Banco de Dados', 'Engenharia de Software I', 'Linguagem de Programação', 'Algoritmos']
        self.label_materia = customtkinter.CTkLabel(self.frame_principal, text="Matéria:")
        self.label_materia.pack(anchor="w")
        self.combo_materia = customtkinter.CTkComboBox(self.frame_principal, values=materias_disponiveis)
        self.combo_materia.pack(fill="x", pady=(0, 10))

        # Campo Data
        self.label_data = customtkinter.CTkLabel(self.frame_principal, text="Data:")
        self.label_data.pack(anchor="w")
        self.entry_data = customtkinter.CTkEntry(self.frame_principal, placeholder_text="DD/MM/AAAA")
        self.entry_data.pack(fill="x", pady=(0, 10))

        # Campo Status (ComboBox)
        status_disponiveis = ['Presente', 'Falta']
        self.label_status = customtkinter.CTkLabel(self.frame_principal, text="Status:")
        self.label_status.pack(anchor="w")
        self.combo_status = customtkinter.CTkComboBox(self.frame_principal, values=status_disponiveis)
        self.combo_status.pack(fill="x", pady=(0, 20))

        # --- BOTÕES ---
        self.frame_botoes = customtkinter.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_botoes.pack(fill="x")

        self.botao_salvar = customtkinter.CTkButton(self.frame_botoes, text="Salvar", command=self.salvar_frequencia)
        self.botao_salvar.pack(side="right", padx=(10, 0))

        self.botao_cancelar = customtkinter.CTkButton(self.frame_botoes, text="Cancelar", fg_color="gray", command=self.destroy)
        self.botao_cancelar.pack(side="right")

        if self.is_edit_mode:
            self._preencher_campos()

    def _center_window(self):
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
        # frequencia_data = ('id', 'aluno', 'ra_aluno', 'materia', 'data', 'status')
        self.combo_aluno.set(self.frequencia_data[1])
        self.combo_materia.set(self.frequencia_data[3])
        self.entry_data.insert(0, self.frequencia_data[4])
        self.combo_status.set(self.frequencia_data[5])

    def salvar_frequencia(self):
        aluno = self.combo_aluno.get()
        materia = self.combo_materia.get()
        data = self.entry_data.get().strip()

        if not all([aluno, materia, data]):
            messagebox.showerror("Erro de Validação", "Todos os campos são obrigatórios.", parent=self)
            return

        print("Salvando frequência...")
        self.parent.atualizar_grid()
        self.destroy()