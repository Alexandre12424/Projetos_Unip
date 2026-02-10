import customtkinter as ctk
from PIL import Image
import os

class PaginaLogin(ctk.CTk):
    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success

        self.title("Login - UniPim")
        self.geometry("360x480") # Tamanho ajustado
        self.resizable(False, False)

        # Aparência
        ctk.set_appearance_mode("system")

        # Centraliza a janela na tela
        self.after(100, self._center_window)

        # Carregar e exibir o logo
        self._carregar_e_exibir_logo()

        # Widgets de login
        self.lbl_bemvindo = ctk.CTkLabel(self, text='Bem-vindo', font=ctk.CTkFont(size=25, weight="bold"))
        self.lbl_bemvindo.pack(pady=(30, 15), padx=20)

        self.campo_usuario = ctk.CTkEntry(self, width=240, placeholder_text='Usuário')
        self.campo_usuario.pack(pady=12, padx=20)

        self.campo_senha = ctk.CTkEntry(self, width=240, placeholder_text='Senha', show='*')
        self.campo_senha.pack(pady=12, padx=20)
        self.campo_senha.bind("<Return>", self.validar_login)

        self.button_login = ctk.CTkButton(self, text='Login', command=self.validar_login, width=240)
        self.button_login.pack(pady=20, padx=20)

        self.resultado_login = ctk.CTkLabel(self, text='', text_color='red')
        self.resultado_login.pack(pady=(0, 10), padx=20)

    def _center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def _carregar_e_exibir_logo(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_dir, '..', 'Assets', 'Logo.png')
            imagem_logo = Image.open(image_path)
            imagem_logo_ctk = ctk.CTkImage(dark_image=imagem_logo, light_image=imagem_logo, size=(144, 44))

            label_logo = ctk.CTkLabel(self, image=imagem_logo_ctk, text='')
            label_logo.pack(pady=(50, 10))
        except FileNotFoundError:
            print("Arquivo de logo não encontrado. Verifique o caminho Assets/Logo.png")
            label_logo = ctk.CTkLabel(self, text='UniPim', font=ctk.CTkFont(size=30, weight="bold"))
            label_logo.pack(pady=(50, 10))

    def validar_login(self, event=None):
        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()
        self.resultado_login.configure(text='Login bem-sucedido!', text_color='green')
        self.after(500, lambda: self._on_success(usuario))
        if usuario == 'admin' and senha == 'admin123':
            self.resultado_login.configure(text='Login bem-sucedido!', text_color='green')
            # Passa o nome de usuário para a função de sucesso
            self.after(500, lambda: self._on_success(usuario))
        else:
            self.resultado_login.configure(text='Usuário ou senha incorretos.', text_color='red')

    def _on_success(self, username):
        self.destroy()
        # Chama o callback passando o nome de usuário
        self.on_login_success(username)
