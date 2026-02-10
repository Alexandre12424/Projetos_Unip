import customtkinter

class JanelaCadastroAluno(customtkinter.CTkToplevel):
    def __init__(self, parent, aluno_data=None):
        super().__init__(parent)
        self.parent = parent
        self.aluno_data = aluno_data

        self.title("Cadastro de Aluno" if aluno_data is None else "Editar Aluno")
        self.geometry("400x400")
        self.resizable(False, False)
        self.after(10, self._center_window)

        # --- Campos do formulário ---
        self.campos = {}
        # Os labels correspondem às colunas do Treeview em vsAlunos.py
        labels = ['RA', 'Nome', 'Curso', 'CPF', 'Data de Nascimento', 'E-mail', 'Telefone']
        
        for i, label_text in enumerate(labels):
            label = customtkinter.CTkLabel(self, text=label_text)
            label.grid(row=i, column=0, padx=20, pady=(10, 0), sticky="w")
            entry = customtkinter.CTkEntry(self, width=200)
            entry.grid(row=i, column=1, padx=20, pady=(10, 0), sticky="ew")
            # Gera uma chave para o dicionário a partir do texto do label
            chave_campo = label_text.lower().replace(' ', '_').replace('ç', 'c').replace('ã', 'a')
            self.campos[chave_campo] = entry

        # Preenche os campos se estiver no modo de edição
        if self.aluno_data:
            self.preencher_campos()

        # --- Frame para os botões ---
        self.frame_botoes_form = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_botoes_form.grid(row=len(labels), column=0, columnspan=2, pady=20)

        self.botao_salvar = customtkinter.CTkButton(self.frame_botoes_form, text="Salvar", command=self.salvar)
        self.botao_salvar.pack(side="left", padx=10)

        self.botao_cancelar = customtkinter.CTkButton(self.frame_botoes_form, text="Cancelar", fg_color="gray", command=self.destroy)
        self.botao_cancelar.pack(side="left", padx=10)

        # Torna a janela modal (bloqueia a interação com a janela principal)
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

    def preencher_campos(self):
        # As chaves devem corresponder às geradas no loop de criação dos campos
        chaves = ['ra', 'nome', 'curso', 'cpf', 'data_de_nascimento', 'e-mail', 'telefone']
        for i, chave in enumerate(chaves):
            if chave in self.campos:
                self.campos[chave].insert(0, self.aluno_data[i])

    def salvar(self):
        dados_formulario = {key: entry.get() for key, entry in self.campos.items()}
        print("Salvando dados:", dados_formulario)
        self.destroy()