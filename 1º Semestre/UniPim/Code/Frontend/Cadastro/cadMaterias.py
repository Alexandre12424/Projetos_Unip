import customtkinter
from tkinter import messagebox

class JanelaCadastroMateria(customtkinter.CTkToplevel):
    def __init__(self, parent, materia_data=None):
        super().__init__(parent)
        self.parent = parent
        self.materia_data = materia_data

        self.is_edit_mode = self.materia_data is not None

        # --- CONFIGURAÇÃO DA JANELA ---
        self.title("Cadastro de Matéria" if not self.is_edit_mode else "Editar Matéria")
        self.geometry("400x300")
        self.resizable(False, False)
        self.after(10, self._center_window)

        # --- WIDGETS ---
        # Campo Nome da Matéria
        self.label_nome = customtkinter.CTkLabel(self, text="Nome da Matéria:")
        self.label_nome.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
        self.entry_nome = customtkinter.CTkEntry(self, width=200, placeholder_text="Ex: Engenharia de Software I")
        self.entry_nome.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="ew")

        # Campo Curso Associado (ComboBox)
        # Idealmente, esta lista viria do banco de dados
        cursos_disponiveis = ['Análise e Des. de Sistemas', 'Ciência da Computação', 'Engenharia de Software']
        self.label_curso = customtkinter.CTkLabel(self, text="Curso Associado:")
        self.label_curso.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="w")
        self.combo_curso = customtkinter.CTkComboBox(self, width=200, values=cursos_disponiveis)
        self.combo_curso.grid(row=1, column=1, padx=20, pady=(10, 0), sticky="ew")

        # Campo Carga Horária
        self.label_carga = customtkinter.CTkLabel(self, text="Carga Horária:")
        self.label_carga.grid(row=2, column=0, padx=20, pady=(10, 0), sticky="w")
        self.entry_carga = customtkinter.CTkEntry(self, width=200, placeholder_text="Ex: 80h")
        self.entry_carga.grid(row=2, column=1, padx=20, pady=(10, 0), sticky="ew")

        # --- BOTÕES ---
        self.frame_botoes = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.grid(row=3, column=0, columnspan=2, pady=30)

        self.botao_salvar = customtkinter.CTkButton(self.frame_botoes, text="Salvar", command=self.salvar_materia)
        self.botao_salvar.pack(side="left", padx=10)

        self.botao_cancelar = customtkinter.CTkButton(self.frame_botoes, text="Cancelar", fg_color="gray", command=self.destroy)
        self.botao_cancelar.pack(side="left", padx=10)

        # Preenche os campos se estiver em modo de edição
        if self.is_edit_mode:
            self._preencher_campos()

        # Torna a janela modal
        self.grab_set()
        self.wait_window()

    def _center_window(self):
        self.update_idletasks()
        # Usamos a janela principal (controller) como referência para centralizar
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
        """Preenche os campos do formulário com os dados da matéria para edição."""
        # materia_data = ('id', 'nome', 'curso', 'carga_horaria')
        self.entry_nome.insert(0, self.materia_data[1])
        self.combo_curso.set(self.materia_data[2])
        self.entry_carga.insert(0, self.materia_data[3])

    def salvar_materia(self):
        """Valida e salva os dados da matéria."""
        nome = self.entry_nome.get().strip()
        curso = self.combo_curso.get()
        carga_horaria = self.entry_carga.get().strip()

        # --- VALIDAÇÃO ---
        if not all([nome, curso, carga_horaria]):
            messagebox.showerror("Erro de Validação", "Todos os campos são obrigatórios.", parent=self)
            return

        # Validação simples para a carga horária
        if not carga_horaria.lower().endswith('h') or not carga_horaria[:-1].isdigit():
            messagebox.showerror("Erro de Validação", "A carga horária deve ser um número seguido de 'h' (ex: 80h).", parent=self)
            return

        # --- LÓGICA DE SALVAMENTO ---
        if self.is_edit_mode:
            # Aqui você implementaria a lógica para atualizar os dados no backend
            print(f"Editando matéria ID {self.materia_data[0]}: {nome}, Curso: {curso}, Carga: {carga_horaria}")
        else:
            # Aqui você implementaria a lógica para inserir um novo registro no backend
            print(f"Adicionando nova matéria: {nome}, Curso: {curso}, Carga: {carga_horaria}")

        # Atualiza o grid na janela principal e fecha a janela de cadastro
        try:
            self.parent.atualizar_grid()
        except Exception as e:
            print(f"Não foi possível atualizar o grid. Erro: {e}")
        
        self.destroy()
