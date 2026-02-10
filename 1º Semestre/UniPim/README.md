# UniPim - Plataforma de Registro Acadêmico Digital

## 🎯 Sobre o Projeto

A **Plataforma de Registro Acadêmico Digital (UniPim)** é um sistema de desktop desenvolvido para modernizar e simplificar a gestão de informações acadêmicas. O projeto substitui o tradicional diário de classe em papel por uma solução eletrônica, permitindo que professores e administradores registrem aulas, notas, presenças e outras atividades de forma mais eficiente.

O sistema é construído com uma arquitetura cliente-servidor, utilizando um backend em **C** para gerenciar a lógica de negócios e um frontend em **Python** com a biblioteca **customtkinter** para a interface do usuário.

## ✨ Funcionalidades

- **Interface Gráfica Moderna:** Interface intuitiva e amigável com temas claro e escuro.
- **Cadastro de Entidades:**
    - Alunos
    - Professores
    - Cursos
    - Matérias
- **Registro de Aulas:** Permite que os professores registrem o conteúdo de cada aula.
- **Comunicação em Rede:** O frontend se comunica com o backend através de sockets TCP para enviar e receber dados em formato JSON.
- **Banco de Dados:** Utiliza **SQLite** para armazenar todas as informações de forma persistente.

## 📂 Estrutura de Pastas

O projeto está organizado da seguinte forma:

```
UniPim/
├── Code/
│   ├── Backend/
│   │   ├── build/                # Contém o executável do servidor
│   │   ├── data/                 # Contém o arquivo do banco de dados
│   │   ├── include/              # Arquivos de cabeçalho C
│   │   └── src/                  # Código-fonte do backend em C
│   └── Frontend/
│       ├── Assets/               # Ícones e imagens da interface
│       ├── Cadastro/             # Módulos de cadastro
│       ├── View/                 # Módulos das telas da aplicação
│       └── main.py               # Ponto de entrada da aplicação frontend
├── Documents/                    # Documentação do projeto
└── README.md                     # Este arquivo
```

## 🔧 Pré-requisitos

Antes de começar, certifique-se de ter os seguintes softwares instalados em sua máquina:

### Backend

- **Compilador C (GCC):** Necessário para compilar o código-fonte do servidor. Você pode instalá-lo através do [MinGW](http://www.mingw.org/) no Windows.

### Frontend

- **Python 3:** A aplicação foi desenvolvida em Python. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).
- **Bibliotecas Python:** Instale as dependências do frontend usando o pip:
  ```bash
  pip install customtkinter Pillow
  ```

## ⚙️ Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto.

### 1. Backend

O backend é responsável por toda a lógica de negócios e comunicação com o banco de dados.

**Compilando o Servidor:**

1.  Abra um terminal na pasta `Code/Backend`.
2.  Execute o seguinte comando para compilar o servidor. O `Makefile` na pasta `src` também pode ser usado com o comando `make`.

    ```bash
    gcc -I include src/servidor.c src/civetweb.c routes/alunos.c utils/response.c -o build/servidor.exe -lws2_32
    gcc -I include -DNO_SSL src/servidor.c src/civetweb.c routes/alunos.c utils/response.c -o build/servidor.exe -lws2_32
    ```

    Este comando compila todos os fontes necessários (`servidor.c`, o `civetweb.c`, a rota de alunos e o utilitário de resposta) e cria o executável `servidor.exe` na pasta `build`.

    **Nota:** Certifique-se de ter os arquivos `civetweb.c` e `civetweb.h` na pasta `src` e `include` respectivamente. Você pode baixá-los do repositório oficial do Civetweb no GitHub.


**Iniciando o Servidor:**

1.  Após a compilação, navegue até a pasta `build`:

    ```bash
    cd build
    ```

2.  Execute o servidor:

    ```bash
    servidor.exe
    ```

    O servidor estará em execução e aguardando conexões na porta `8080`.

### 2. Frontend

O frontend é a interface gráfica com a qual o usuário interage.

**Executando a Aplicação:**

1.  Abra um novo terminal e navegue até a pasta `Code/Frontend`:

    ```bash
    cd Code/Frontend
    ```

2.  Execute o arquivo `main.py` para iniciar a aplicação:

    ```bash
    python main.py
    ```

    A janela de login será exibida. Após o login, a aplicação principal será carregada.

## 🗃️ Banco de Dados

O sistema utiliza o **SQLite** como banco de dados. O arquivo do banco de dados, `unipim.db`, é criado automaticamente na pasta `Code/Backend/data` quando o servidor é iniciado pela primeira vez.

A tabela principal é a `aulas`, com a seguinte estrutura:

| Coluna      | Tipo     | Descrição                               |
|-------------|----------|-------------------------------------------|
| `id`        | INTEGER  | Identificador único da aula (autoincremento) |
| `turma`     | TEXT     | Nome da turma                             |
| `professor` | TEXT     | Nome do professor                         |
| `conteudo`  | TEXT     | Conteúdo da aula ministrada               |
| `timestamp` | DATETIME | Data e hora do registro da aula           |

## 📡 API (Comunicação Backend)

A comunicação entre o frontend e o backend é feita via sockets TCP, com mensagens no formato JSON. O servidor escuta na porta `5050` e espera por requisições JSON com a seguinte estrutura:

```json
{
  "acao": "nome_da_acao",
  "dados": {
    "chave": "valor"
  }
}
```

### Ações Disponíveis

#### `registrar_aula`

Registra uma nova aula no banco de dados.

**Requisição:**

```json
{
  "acao": "registrar_aula",
  "turma": "Nome da Turma",
  "professor": "Nome do Professor",
  "conteudo": "Conteúdo da aula"
}
```

**Resposta (Sucesso):**

```json
{
  "status": "sucesso",
  "mensagem": "Aula registrada com sucesso!"
}
```

**Resposta (Erro):**

```json
{
  "status": "erro",
  "mensagem": "Mensagem de erro detalhada."
}
```

#### `listar_aulas`

Retorna uma lista de todas as aulas registradas.

**Requisição:**

```json
{
  "acao": "listar_aulas"
}
```

**Resposta (Sucesso):**

```json
{
  "status": "sucesso",
  "aulas": [
    {
      "id": 1,
      "turma": "Engenharia de Software",
      "professor": "Dr. Alan Turing",
      "conteudo": "Introdução a algoritmos.",
      "timestamp": "2025-10-20 10:00:00"
    },
    {
      "id": 2,
      "turma": "Ciência de Dados",
      "professor": "Dr. Ada Lovelace",
      "conteudo": "Análise exploratória de dados.",
      "timestamp": "2025-10-20 11:00:00"
    }
  ]
}
```