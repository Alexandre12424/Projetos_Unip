#include "civetweb.h"
#include "../include/response.h"
#include <string.h>

int alunos_handler(struct mg_connection *conn, void *cbdata)
{
  const struct mg_request_info *req_info = mg_get_request_info(conn);

  if (strcmp(req_info->request_method, "GET") == 0)
  {
    const char *json = "{\"alunos\": [{\"id\":1, \"nome\":\"João\"}, {\"id\":2, \"nome\":\"Maria\"}]}";
    send_json(conn, 200, json);
    return 200;
  }

  send_json(conn, 405, "{\"erro\": \"Método não permitido\"}");
  return 405;
}
