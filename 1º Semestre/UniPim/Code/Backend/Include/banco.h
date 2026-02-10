#ifndef BANCO_H
#define BANCO_H

#include "sqlite3.h"
#include "cJSON.h"

// Funções exportadas para serem usadas pelo servidor
int inicializar_banco(sqlite3 **db);
int registrar_aula(sqlite3 *db, const char *turma, const char *professor, const char *conteudo);
int listar_aulas(sqlite3 *db, cJSON *array_aulas);
void fechar_banco(sqlite3 *db);

#endif // BANCO_H