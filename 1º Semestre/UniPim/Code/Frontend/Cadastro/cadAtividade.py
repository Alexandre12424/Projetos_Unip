import customtkinter
from tkinter import messagebox

class JanelaCadastroAtividade(customtkinter.CTkToplevel):
    def __init__(self, parent, atividade_data=None):
        super().__init__(parent)
        self.parent = parent
        self.atividade_data = atividade_data

        # --- CONFIGURAÇÃO DA JANELA ---
        self.title("Cadastro de Atividade" if atividade_data is None else "Editar Atividade")
        self.geometry("400x280")
        self.transient(parent)
        self.grab_set()
        self.resizable(False, False)
        
        self.after(10, self._center_window)

        self.is_edit_mode = self.atividade_data is not None

        # --- WIDGETS ---
        self.frame_principal = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_principal.pack(expand=True, fill="both", padx=20, pady=20)

        # Campo Título da Atividade
        self.label_titulo = customtkinter.CTkLabel(self.frame_principal, text="Título:")
        self.label_titulo.pack(anchor="w")
        self.entry_titulo = customtkinter.CTkEntry(self.frame_principal, placeholder_text="Ex: Trabalho de Banco de Dados")
        self.entry_titulo.pack(fill="x", pady=(0, 10))

        # Campo Matéria (ComboBox)
        materias_disponiveis = ['Banco de Dados', 'Engenharia de Software I', 'Linguagem de Programação']
        self.label_materia = customtkinter.CTkLabel(self.frame_principal, text="Matéria:")
        self.label_materia.pack(anchor="w")
        self.combo_materia = customtkinter.CTkComboBox(self.frame_principal, values=materias_disponiveis)
        self.combo_materia.pack(fill="x", pady=(0, 20))

        # Campo Data de Entrega
        self.label_data = customtkinter.CTkLabel(self.frame_principal, text="Data de Entrega:")
        self.label_data.pack(anchor="w")
        self.entry_data = customtkinter.CTkEntry(self.frame_principal, placeholder_text="DD/MM/AAAA")
        self.entry_data.pack(fill="x", pady=(0, 20))

        # --- BOTÕES ---
        self.frame_botoes = customtkinter.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_botoes.pack(fill="x")

        self.botao_salvar = customtkinter.CTkButton(self.frame_botoes, text="Salvar", command=self.salvar_atividade)
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
        """Preenche os campos com os dados da atividade para edição."""
        # atividade_data = ('id', 'titulo', 'materia', 'data_entrega')
        self.entry_titulo.insert(0, self.atividade_data[1])
        self.combo_materia.set(self.atividade_data[2])
        self.entry_data.insert(0, self.atividade_data[3])

    def salvar_atividade(self):
        """Valida e salva os dados da atividade."""
        titulo = self.entry_titulo.get().strip()
        data = self.entry_data.get().strip()

        if not all([titulo, data]):
            messagebox.showerror("Erro de Validação", "Os campos 'Título' e 'Data de Entrega' são obrigatórios.", parent=self)
            return

        print("Salvando atividade...")
        self.parent.atualizar_grid()
        self.destroy()
