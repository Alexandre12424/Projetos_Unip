import customtkinter
from tkinter import ttk
import os
import sys

# Adiciona o diretório 'Code' ao sys.path para resolver os imports relativos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PIL import Image
from View.vsLogin import PaginaLogin
from View.vsPadrao import PaginaInicio
from View.vsAlunos import PaginaAlunos
from View.vsProfessores import PaginaProfessores
from View.vsConfigs import PaginaConfiguracoes
from View.vsMaterias import PaginaMaterias
from View.vsCursos import PaginaCursos
from View.vsUsuarios import PaginaUsuarios
from View.vsSalas import PaginaSalas
from View.vsAtividades import PaginaAtividades
from View.vsProvas import PaginaProvas
from View.vsFrequencia import PaginaFrequencia

class UniPimApp(customtkinter.CTk):

    def __init__(self, *args, usuario_logado="Usuário Padrão", **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario_logado = usuario_logado

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.title("UniPim - Plataforma de registro acadêmico digital")

        self.after(0, lambda: self.state('zoomed'))

        self.tema_atual = "dark"

        # Dicionário para mapear nome dos temas em português
        self.mapa_temas = {"Escuro": "dark", "Claro": "light", "Sistema": "system"}
        
        # Dicionário para mapear cores de tema
        self.mapa_cores = {"Azul": "blue", "Verde": "green", "Dark Blue": "dark-blue"}

        style = ttk.Style(self)
        style.theme_use("clam")

        self.ribbon_container = customtkinter.CTkFrame(self, corner_radius=0)
        self.ribbon_container.pack(side="top", fill="x")

        self.container_conteudo = customtkinter.CTkFrame(self, corner_radius=0, fg_color=("#dbdbdb", "#2b2b2b"))
        self.container_conteudo.pack(side="top", expand=True, fill="both")
        
        self.criar_interface_ribbon()

        # --- NOVO SISTEMA DE ABAS ---
        self.tab_header_frame = customtkinter.CTkFrame(self.container_conteudo, height=30, corner_radius=0, fg_color="transparent")
        self.tab_header_frame.pack(side="top", fill="x", padx=5, pady=(5, 0))

        self.tab_content_frame = customtkinter.CTkFrame(self.container_conteudo, corner_radius=0, fg_color="transparent")
        self.tab_content_frame.pack(side="top", expand=True, fill="both", padx=5, pady=(0, 5))

        self.abas_abertas = {}
        self.aba_ativa_nome = None
        # Track selected buttons for persistent visual state
        self.selected_ribbon_button = None
        self.selected_action_button = None

        # A PaginaConfiguracoes é tratada separadamente para sobrepor as abas do ribbon
        self.pagina_config = PaginaConfiguracoes(self.container_conteudo, self)

        self.criar_barra_status()
        self.atualizar_estilo_treeview()

    def mostrar_pagina(self, page_class):
        if page_class == PaginaConfiguracoes:
            self.pagina_config.tkraise()
            self.pagina_config.place(relwidth=1, relheight=1)
        else:
            self.pagina_config.place_forget()
            
            # Lógica para abrir ou focar na aba correspondente
            nome_aba = self.obter_nome_aba(page_class)
            self.abrir_ou_focar_aba(page_class, nome_aba)

    def _criar_botao_de_aba(self, nome_aba):
        """Cria o botão que representa uma aba no cabeçalho."""
        tab_button_frame = customtkinter.CTkFrame(self.tab_header_frame, corner_radius=6, fg_color="transparent", border_width=1)
        tab_button_frame.pack(side="left", fill="y", padx=(0, 2))

        label_button = customtkinter.CTkButton(
            tab_button_frame,
            text=nome_aba,
            corner_radius=6,
            command=lambda n=nome_aba: self.ativar_aba_visual(n),
            fg_color="transparent",
            text_color=("gray10", "gray90")
        )
        label_button.pack(side="left", padx=(6, 0), pady=2)

        close_button = None
        close_button = customtkinter.CTkButton(
            tab_button_frame,
            text="✕",
            width=24,
            height=24,
            corner_radius=6,
            command=lambda n=nome_aba: self.fechar_aba(n),
            fg_color="transparent",
            hover_color=("#e0e0e0", "#3d3d3d"),
            text_color=("gray10", "gray90")
        )
        close_button.pack(side="left", padx=(2, 6), pady=2)
        
        return tab_button_frame, label_button, close_button

    def abrir_ou_focar_aba(self, page_class, nome_aba):
        """Cria uma nova aba se não existir, ou foca nela se já estiver aberta."""
        if nome_aba in self.abas_abertas:
            self.ativar_aba_visual(nome_aba)
        else:
            pagina = page_class(self.tab_content_frame, self)
            tab_button_frame, label_button, close_button = self._criar_botao_de_aba(nome_aba)

            self.abas_abertas[nome_aba] = {
                "pagina": pagina, 
                "classe": page_class,
                "button_frame": tab_button_frame,
                "label_button": label_button
            }
            self.ativar_aba_visual(nome_aba)

    def fechar_aba(self, nome_aba):
        """Fecha a aba especificada."""
        if nome_aba in self.abas_abertas:
            aba_a_fechar = self.abas_abertas[nome_aba]
            aba_a_fechar["pagina"].destroy()
            aba_a_fechar["button_frame"].destroy()
            del self.abas_abertas[nome_aba]

            # Se a aba fechada era a ativa, ativa a última aba da lista ou a de Início
            if self.aba_ativa_nome == nome_aba:
                if self.abas_abertas:
                    proxima_aba = list(self.abas_abertas.keys())[-1]
                    self.ativar_aba_visual(proxima_aba)
                else:
                    self.aba_ativa_nome = None

    def criar_interface_ribbon(self):
        self.tab_bar = customtkinter.CTkFrame(self.ribbon_container, corner_radius=0)
        self.tab_bar.pack(side="top", fill="x", padx=5, pady=(5, 0))

        self.ribbon_content_area = customtkinter.CTkFrame(self.ribbon_container, height=110)
        self.ribbon_content_area.pack(side="top", fill="x")
        self.ribbon_content_area.pack_propagate(False)

        self.ribbon_frames = {}
        icones_abas = {
            "Cadastros": "Assets/Cadastros.png",
            "Atividades e Avaliações": "Assets/AtividadesProvas.png",
            "Relatórios": "Assets/Relatorios.png"
        }

        abas_esquerda = ["Cadastros", "Atividades e Avaliações", "Relatórios"]
        for aba_nome in abas_esquerda:
            frame = customtkinter.CTkFrame(self.ribbon_content_area)
            self.ribbon_frames[aba_nome] = frame
            frame.place(relwidth=1, relheight=1)
            self.criar_botao_aba(self.tab_bar, aba_nome, icones_abas.get(aba_nome), lambda f=frame, name=aba_nome: self.ativar_aba(f, name))

        # --- Widgets da Direita ---
        self.criar_botao_utilitario(self.tab_bar, "Sair", "Assets/Sair.png", self.quit, width=80, fg_color="#D2042D", hover_color="#A50021")
        self.criar_botao_utilitario(self.tab_bar, "Configurações", "Assets/Config.png", lambda: self.mostrar_pagina(PaginaConfiguracoes), width=140)

        self.adicionar_botoes_ribbon_cadastros()
        self.adicionar_botoes_ribbon_atividades()
        
        self.tab_buttons = {w.cget("text"): w for w in self.tab_bar.winfo_children() 
                            if isinstance(w, customtkinter.CTkButton) and w.cget("text") in abas_esquerda}

        # Ativa as abas do ribbon. A última chamada será a aba visível no início.
        self.ativar_aba(self.ribbon_frames["Atividades e Avaliações"], "Atividades e Avaliações")
        self.ativar_aba(self.ribbon_frames["Cadastros"], "Cadastros") # Esta será a aba padrão ao iniciar

    def ativar_aba_visual(self, nome_aba):
        """Mostra o conteúdo de uma aba e atualiza o estilo dos botões."""
        self.aba_ativa_nome = nome_aba
        
        # Atualiza o estilo dos botões de aba
        for nome, data in self.abas_abertas.items(): # type: ignore
            if nome == nome_aba:
                data["button_frame"].configure(fg_color=("#ffffff", "#333333"))
                data["label_button"].configure(font=customtkinter.CTkFont(weight="bold"))
            else:
                data["button_frame"].configure(fg_color="transparent")
                data["label_button"].configure(font=customtkinter.CTkFont(weight="normal"))

        # Esconde todas as páginas
        for data in self.abas_abertas.values():
            data["pagina"].pack_forget()

        pagina_para_ativar = self.abas_abertas[nome_aba]["pagina"]
        pagina_para_ativar.pack(expand=True, fill="both")

    def ativar_aba(self, frame_para_ativar, nome_aba):
        self.aba_ativa = nome_aba
        frame_para_ativar.tkraise()
        self.atualizar_estilo_abas()
        # Update visual selection for ribbon buttons so the clicked tab stays highlighted
        try:
            # Find the button in the tab_bar with matching text and mark it selected
            for w in self.tab_bar.winfo_children():
                if isinstance(w, customtkinter.CTkButton) and w.cget("text") == nome_aba:
                    # Unselect previous
                    if self.selected_ribbon_button and self.selected_ribbon_button is not w:
                        self.selected_ribbon_button.configure(text_color=("gray10", "gray90"), border_width=0)
                    # Select new
                    w.configure(text_color="#2d6cdf", border_width=1, border_color="#2d6cdf")
                    self.selected_ribbon_button = w
                    break
        except Exception:
            pass

    def atualizar_estilo_abas(self):
        for nome, botao in self.tab_buttons.items():
            if nome == self.aba_ativa:
                botao.configure(border_width=0)
            else:
                botao.configure(border_width=0)

    def adicionar_botoes_ribbon_cadastros(self):
        self.criar_botao_acao(self.ribbon_frames["Cadastros"], "Usuários", "Assets/Usuario.png", lambda: self.mostrar_pagina(PaginaUsuarios))
        self.criar_botao_acao(self.ribbon_frames["Cadastros"], "Alunos", "Assets/Aluno.png", lambda: self.mostrar_pagina(PaginaAlunos))
        self.criar_botao_acao(self.ribbon_frames["Cadastros"], "Professores", "Assets/Professor.png", lambda: self.mostrar_pagina(PaginaProfessores))
        self.criar_botao_acao(self.ribbon_frames["Cadastros"], "Cursos", "Assets/Curso.png", lambda: self.mostrar_pagina(PaginaCursos))
        self.criar_botao_acao(self.ribbon_frames["Cadastros"], "Matérias", "Assets/Materias.png", lambda: self.mostrar_pagina(PaginaMaterias))
        self.criar_botao_acao(self.ribbon_frames["Cadastros"], "Salas", "Assets/Sala.png", lambda: self.mostrar_pagina(PaginaSalas))

    def adicionar_botoes_ribbon_atividades(self):
        self.criar_botao_acao(self.ribbon_frames["Atividades e Avaliações"], "Atividades", "Assets/Atividades.png", lambda: self.mostrar_pagina(PaginaAtividades))
        self.criar_botao_acao(self.ribbon_frames["Atividades e Avaliações"], "Provas", "Assets/Provas.png", lambda: self.mostrar_pagina(PaginaProvas))
        self.criar_botao_acao(self.ribbon_frames["Atividades e Avaliações"], "Registro de Frequência", "Assets/Frequencia.png", lambda: self.mostrar_pagina(PaginaFrequencia))

    def obter_nome_aba(self, page_class):
        """Retorna o nome de exibição para uma classe de página."""
        nomes = {
            PaginaUsuarios: "Usuários",
            PaginaAlunos: "Alunos",
            PaginaProfessores: "Professores",
            PaginaCursos: "Cursos",
            PaginaMaterias: "Matérias",
            PaginaSalas: "Salas",
            PaginaInicio: "Início",
            PaginaAtividades: "Atividades",
            PaginaProvas: "Provas",
            PaginaFrequencia: "Frequência"
        }
        return nomes.get(page_class, "Nova Aba")

    def criar_botao_aba(self, parent, texto, caminho_icone, comando):
        ctk_image = None
        try:
            if caminho_icone:
                script_dir = os.path.dirname(os.path.abspath(__file__))
                caminho_completo = os.path.join(script_dir, caminho_icone)
                ctk_image = customtkinter.CTkImage(
                    light_image=Image.open(caminho_completo),
                    dark_image=Image.open(caminho_completo),
                    size=(20, 20)
                )
        except FileNotFoundError:
            print(f"Aviso: Ícone da aba não encontrado em '{caminho_icone}'.")

        botao = customtkinter.CTkButton(parent, 
                                        text=texto, 
                                        command=comando,
                                        image=ctk_image,
                                        compound="left",
                                        font=customtkinter.CTkFont(size=13),
                                        fg_color="transparent",
                                        border_width=0,
                                        text_color=("gray10", "gray90"))
        botao.pack(side="left", padx=2)

        # Hover: change text color to blue and show border; revert on leave unless selected
        def _on_enter(event, b=botao):
            try:
                if self.selected_ribbon_button is not b:
                    b.configure(text_color="#2d6cdf", border_width=1, border_color="#2d6cdf")
            except Exception:
                pass

        def _on_leave(event, b=botao):
            try:
                if self.selected_ribbon_button is not b:
                    b.configure(text_color=("gray10", "gray90"), border_width=0)
            except Exception:
                pass

        botao.bind('<Enter>', _on_enter)
        botao.bind('<Leave>', _on_leave)
        return botao

    def criar_botao_utilitario(self, parent, texto, caminho_icone, comando, **kwargs):
        ctk_image = None
        try:
            if caminho_icone:
                script_dir = os.path.dirname(os.path.abspath(__file__))
                caminho_completo = os.path.join(script_dir, caminho_icone)
                ctk_image = customtkinter.CTkImage(
                    light_image=Image.open(caminho_completo),
                    dark_image=Image.open(caminho_completo),
                    size=(20, 20)
                )
        except FileNotFoundError:
            print(f"Aviso: Ícone não encontrado em '{caminho_icone}'.")

        botao = customtkinter.CTkButton(
            parent,
            text=texto,
            command=comando,
            image=ctk_image,
            **kwargs)
        botao.pack(side="right", padx=2)

    def criar_botao_acao(self, parent, texto, caminho_icone, comando, pack_side="left"):
        ctk_image = None
        try:
            if caminho_icone:
                script_dir = os.path.dirname(os.path.abspath(__file__))
                caminho_completo = os.path.join(script_dir, caminho_icone)
                ctk_image = customtkinter.CTkImage(
                    light_image=Image.open(caminho_completo),
                    dark_image=Image.open(caminho_completo),
                    size=(40, 40)
                )
        except FileNotFoundError:
            print(f"Aviso: Ícone não encontrado em '{caminho_icone}'. Criando botão sem imagem.")

        botao = customtkinter.CTkButton(
            parent, 
            text=texto, 
            command=comando, 
            image=ctk_image, 
            compound="top", 
            font=customtkinter.CTkFont(size=14),
            fg_color="transparent",
            text_color=("gray10", "gray90"))
        botao.pack(side=pack_side, padx=1, pady=0)

        # Hover effect for action buttons
        def _on_enter_action(event, b=botao):
            try:
                if self.selected_action_button is not b:
                    b.configure(text_color="#2d6cdf", border_width=1, border_color="#2d6cdf")
            except Exception:
                pass

        def _on_leave_action(event, b=botao):
            try:
                if self.selected_action_button is not b:
                    b.configure(text_color=("gray10", "gray90"), border_width=0)
            except Exception:
                pass

        botao.bind('<Enter>', _on_enter_action)
        botao.bind('<Leave>', _on_leave_action)

        # Wrap the original command so the button remains selected until another is clicked
        original_command = comando
        def _on_click_action(b=botao):
            try:
                # Unselect previous
                if self.selected_action_button and self.selected_action_button is not b:
                    try:
                        self.selected_action_button.configure(text_color=("gray10", "gray90"), border_width=0)
                    except Exception:
                        pass
                # Select this button
                b.configure(text_color="#2d6cdf", border_width=1, border_color="#2d6cdf")
                self.selected_action_button = b
            except Exception:
                pass
            # Finally call the original action
            try:
                original_command()
            except Exception:
                pass

        botao.configure(command=_on_click_action)
        return botao
    
    def trocar_tema_combobox(self, tema_em_portugues: str):
        novo_tema = self.mapa_temas[tema_em_portugues]
        customtkinter.set_appearance_mode(novo_tema)
        
        # Se o tema for 'system', precisamos descobrir qual tema o sistema está usando de fato.
        if novo_tema == "system":
            # _get_appearance_mode() retorna 'dark' ou 'light'
            self.tema_atual = customtkinter.get_appearance_mode().lower()
        else:
            self.tema_atual = novo_tema

        self.atualizar_estilo_treeview()

    def trocar_cor_tema(self, cor_em_portugues: str):
        nova_cor = self.mapa_cores[cor_em_portugues]
        customtkinter.set_default_color_theme(nova_cor)
        # É necessário recriar a interface ou reiniciar para que todas as cores sejam aplicadas

    def alterar_tamanho_fonte(self, tamanho: str):
        # Esta função é um placeholder. A lógica para alterar a fonte em toda a UI precisa ser implementada.
        print(f"Alterar tamanho da fonte para: {tamanho}")

    def atualizar_estilo_treeview(self):
        if self.tema_atual.lower() == "dark":
            bg_color = "#2B2B2B" # Cinza neutro, padrão do CustomTkinter
            text_color = "white"
            field_bg_color = "#333333" # Cinza escuro mais neutro
            header_bg = "#444444" # Cinza médio mais neutro
            selected_color = "#22559b"
            header_border_color = "#444444" # Cor da borda igual ao fundo para um visual uniforme
        else: # Tema claro
            bg_color = "#ebebeb"
            text_color = "black"
            field_bg_color = "#f2f2f2"
            header_bg = "#d6d6d6"
            selected_color = "#3a7ebf"
            header_border_color = "#d6d6d6" # Cor da borda igual ao fundo para um visual uniforme

        style = ttk.Style()
        style.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=field_bg_color, borderwidth=0)
        style.map('Treeview', background=[('selected', selected_color)])
        style.configure("Treeview.Heading", background=header_bg, foreground=text_color, relief="flat", borderwidth=1, bordercolor=header_border_color)
        style.map("Treeview.Heading", background=[('active', '#3484F0')])
    
    def criar_barra_status(self):
        """Cria e configura a barra de status na parte inferior da janela."""
        self.status_bar = customtkinter.CTkFrame(self, height=25, corner_radius=0)
        self.status_bar.pack(side="bottom", fill="x")

        self.label_usuario = customtkinter.CTkLabel(
            self.status_bar, text=f"Usuário: {self.usuario_logado}", anchor="w", font=customtkinter.CTkFont(size=12)
        )
        self.label_usuario.pack(side="left", padx=(10, 0))

        self.label_versao = customtkinter.CTkLabel(self.status_bar, text="Versão: 1.0.0-beta", anchor="e", font=customtkinter.CTkFont(size=12))
        self.label_versao.pack(side="right", padx=(0, 10))


if __name__ == "__main__":
    def start_main_app(usuario="Não identificado"):
        app = UniPimApp(usuario_logado=usuario)
        app.mainloop()

    def on_login_success_callback(username):
        start_main_app(usuario=username)

    login_app = PaginaLogin(on_login_success=on_login_success_callback)
    login_app.mainloop()