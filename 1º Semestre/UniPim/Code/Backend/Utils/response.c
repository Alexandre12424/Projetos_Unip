#include "civetweb.h"
#include "response.h"

void send_json(struct mg_connection *conn, int status, const char *json)
{
  mg_printf(conn,
            "HTTP/1.1 %d OK\r\n"
            "Content-Type: application/json\r\n"
            "Content-Length: %zu\r\n\r\n%s",
            status, strlen(json), json);
}
