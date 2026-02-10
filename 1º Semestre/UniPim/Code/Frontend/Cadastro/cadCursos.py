import customtkinter

class JanelaCadastroCurso(customtkinter.CTkToplevel):
    def __init__(self, parent, curso_data=None):
        super().__init__(parent)
        self.parent = parent
        self.curso_data = curso_data

        self.title("Cadastro de Curso" if curso_data is None else "Editar Curso")
        self.geometry("400x300")
        self.resizable(False, False)
        self.after(10, self._center_window)

        # --- Campos do formulário ---
        self.campos = {}
        # Os labels correspondem aos cabeçalhos do Treeview em vsCursos.py
        labels = ['ID', 'Nome do Curso', 'Coordenador', 'Duração (Semestres)']
        
        for i, label_text in enumerate(labels):
            label = customtkinter.CTkLabel(self, text=label_text)
            label.grid(row=i, column=0, padx=20, pady=(10, 0), sticky="w")
            entry = customtkinter.CTkEntry(self, width=200)
            entry.grid(row=i, column=1, padx=20, pady=(10, 0), sticky="ew")
            # Gera uma chave para o dicionário a partir do texto do label
            chave_campo = label_text.lower().replace(' ', '_').replace('ç', 'c').replace('ã', 'a').replace('(', '').replace(')', '')
            self.campos[chave_campo] = entry

        # Preenche os campos se estiver no modo de edição
        if self.curso_data:
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
        # O wait_window() já é chamado implicitamente pela forma como a janela é criada em vsCursos.py

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
        chaves = ['id', 'nome_do_curso', 'coordenador', 'duracao_semestres']
        for i, chave in enumerate(chaves):
            if chave in self.campos:
                self.campos[chave].insert(0, self.curso_data[i])

    def salvar(self):
        dados_formulario = {key: entry.get() for key, entry in self.campos.items()}
        
        # Aqui você adicionaria a lógica para validar e salvar os dados no backend
        if self.curso_data:
            print("Editando dados do curso:", dados_formulario)
        else:
            print("Salvando novo curso:", dados_formulario)

        # A atualização do grid já é chamada em vsCursos.py após esta janela ser fechada.
        self.destroy()