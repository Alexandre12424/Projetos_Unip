#include <stdio.h>
#include <string.h>
#include "../include/civetweb.h"
#include "../include/routes.h"

int main(void)
{
  struct mg_context *ctx;
  // Nota: A porta agora é uma string.
  // O "r" no final de 8080r significa que a porta pode ser reutilizada.
  // O "s" (ex: 8080s) ativaria SSL/TLS se os certificados estivessem configurados.
  const char *options[] = {
      "listening_ports", "8080",
      "document_root", ".", // Opcional: para servir arquivos estáticos
      "num_threads", "4",   // Opcional: número de threads de trabalho
      NULL};

  // Inicializa a biblioteca Civetweb
  mg_init_library(0);

  // Inicia o servidor web
  ctx = mg_start(NULL, 0, options);
  if (ctx == NULL)
  {
    fprintf(stderr, "Erro ao iniciar o servidor Civetweb.\n");
    return 1;
  }

  printf("Servidor Civetweb iniciado em http://localhost:8080\n");

  // --- REGISTRO DAS ROTAS DA API ---
  // Todas as rotas da API começarão com /api/ para organização
  mg_set_request_handler(ctx, "/api/alunos", alunos_handler, 0);
  // Adicione outras rotas aqui no futuro, por exemplo:
  // mg_set_request_handler(ctx, "/api/professores", professores_handler, 0);
  // mg_set_request_handler(ctx, "/api/salas", salas_handler, 0);

  printf("Rota /api/alunos registrada.\n");
  printf("Pressione Enter para sair...\n");

  // Mantém o servidor rodando até que o usuário pressione Enter
  getchar();

  // Para o servidor
  mg_stop(ctx);
  printf("Servidor parado.\n");

  // Libera recursos da biblioteca
  mg_exit_library();

  return 0;
}
