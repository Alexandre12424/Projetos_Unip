#ifndef RESPONSE_H
#define RESPONSE_H

#include "civetweb.h"

void send_json(struct mg_connection *conn, int status, const char *json);

#endif // RESPONSE_H