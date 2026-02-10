import customtkinter

class PaginaConfiguracoes(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.label = customtkinter.CTkLabel(self, text="Página de Configurações", font=customtkinter.CTkFont(size=18))
        self.label.pack(pady=20, padx=20)

        # Frame para o seletor de tema
        self.frame_tema = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_tema.pack(pady=10, padx=20, anchor="w")

        # Label para o tema
        self.label_tema = customtkinter.CTkLabel(self.frame_tema, text="Tema da Aplicação:")
        self.label_tema.pack(side="left", padx=(0, 10))

        # ComboBox para seleção de tema
        # Acessa o mapa_temas e a função de troca de tema do controller (UniPimApp)
        temas_disponiveis_pt = list(self.controller.mapa_temas.keys())
        self.combo_tema = customtkinter.CTkComboBox(self.frame_tema, 
                                                    values=temas_disponiveis_pt, 
                                                    command=self.controller.trocar_tema_combobox, 
                                                    width=150)
        self.combo_tema.set([k for k, v in self.controller.mapa_temas.items() if v == self.controller.tema_atual][0])
        self.combo_tema.pack(side="left")

        # --- Frame para o seletor de tamanho da fonte ---
        self.frame_fonte = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_fonte.pack(pady=10, padx=20, anchor="w")

        self.label_fonte = customtkinter.CTkLabel(self.frame_fonte, text="Tamanho da Fonte:")
        self.label_fonte.pack(side="left", padx=(0, 10))

        self.combo_fonte = customtkinter.CTkComboBox(self.frame_fonte,
                                             values=["Pequeno", "Médio", "Grande"],
                                             command=self.controller.alterar_tamanho_fonte, # Lembre-se que esta função é um placeholder
                                             width=150)
        self.combo_fonte.set("Médio")
        self.combo_fonte.pack(side="left")

        # --- Frame para o seletor de cor de destaque ---
        self.frame_cor = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_cor.pack(pady=10, padx=20, anchor="w")

        # Label para a cor
        self.label_cor = customtkinter.CTkLabel(self.frame_cor, text="Cor de Destaque:")
        self.label_cor.pack(side="left", padx=(0, 10))

        # ComboBox para seleção de cor
        cores_disponiveis_pt = list(self.controller.mapa_cores.keys())
        self.combo_cor = customtkinter.CTkComboBox(self.frame_cor,
                                                   values=cores_disponiveis_pt,
                                                   command=self.controller.trocar_cor_tema,
                                                   width=150)
        self.combo_cor.set("Azul") # Define o valor padrão
        self.combo_cor.pack(side="left")
