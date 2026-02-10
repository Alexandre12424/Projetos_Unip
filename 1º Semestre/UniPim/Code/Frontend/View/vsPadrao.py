import customtkinter

class PaginaInicio(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Você pode adicionar um label de boas-vindas aqui se quiser
        label = customtkinter.CTkLabel(self, text="", 
                                       font=customtkinter.CTkFont(size=24, weight="bold"))
        label.pack(pady=50, padx=20)
