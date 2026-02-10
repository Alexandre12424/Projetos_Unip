#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cJSON.h"   // Incluir para manipulação de JSON
#include "sqlite3.h" // Incluir a biblioteca do SQLite
#include "banco.h"   // Incluir nosso próprio cabeçalho

#define DB_FILE "C:\\Users\\Usuario\\OneDrive\\Documentos\\1_teste_massari\\aula\\Include\\unipim.db" // Caminho correto para o arquivo do banco

int inicializar_banco(sqlite3 **db)
{
  char *erro = NULL;
  int rc = sqlite3_open(DB_FILE, db);
  if (rc != SQLITE_OK)
  {
    fprintf(stderr, "Nao foi possivel abrir o banco de dados: %s\n", sqlite3_errmsg(*db));
    sqlite3_close(*db);
    return 1; // Retornar 1 para erro, 0 para sucesso
  }
return 0;
}

void fechar_banco(sqlite3 *db)
{
  sqlite3_close(db);
}
//=================================CRUD USUARIO=================================//
//---------------Criar USUARIO------------
int inserir_usuario(sqlite3 *db, const char *nome, const char *email, const char *senha, const char *tipo, const char *dtcadastro, int status){
    const char *sql = "INSERT INTO USUARIO (NOME, EMAIL, SENHA, TIPOUSUARIO, DTCADASTRO, STATUS) VALUES (?, ?, ?, ?, ?, ?);";
    sqlite3_stmt *stmt;

int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar INSERT: %s\n", sqlite3_errmsg(db));
        return 1;
    }

  sqlite3_bind_text(stmt, 1, nome, -1, SQLITE_TRANSIENT);
  sqlite3_bind_text(stmt, 2, email, -1, SQLITE_TRANSIENT);
  sqlite3_bind_text(stmt, 3, senha, -1, SQLITE_TRANSIENT);
  sqlite3_bind_text(stmt, 4, tipo, -1, SQLITE_TRANSIENT);
  sqlite3_bind_text(stmt, 5, dtcadastro, -1, SQLITE_TRANSIENT);
  sqlite3_bind_int(stmt, 6, status);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);

  return rc == SQLITE_DONE ? 0 : 1;

  }
//---------------Listar USUARIO------------
int listar_usuario(sqlite3 *db) {
    const char *sql = "SELECT IDUSUARIO, NOME, EMAIL, TIPOUSUARIO, DTCADASTRO, STATUS FROM USUARIO;";

    sqlite3_stmt *stmt;
    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar SELECT: %s\n", sqlite3_errmsg(db));
        return 1;
    }

    printf("Lista de usuários:\n");
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
        printf("ID: %d | Nome: %s | Email: %s | Tipo: %s | Cadastro: %s | Status: %d\n",
               sqlite3_column_int(stmt, 0),
               sqlite3_column_text(stmt, 1),
               sqlite3_column_text(stmt, 2),
               sqlite3_column_text(stmt, 3),
               sqlite3_column_text(stmt, 4),
               sqlite3_column_int(stmt, 5));
    }
    sqlite3_finalize(stmt);
    return 0;
}
//---------------Atualizar USUARIO------------
  int atualizar_usuario(sqlite3 *db, int id, const char *novo_nome, const char *novo_email, const char *nova_senha, int novo_status) {
    const char *sql = "UPDATE USUARIO SET NOME = ?, EMAIL = ?, SENHA = ?, STATUS = ? WHERE IDUSUARIO = ?;";
    sqlite3_stmt *stmt;

    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar UPDATE: %s\n", sqlite3_errmsg(db));
        return 1;
    }

    sqlite3_bind_text(stmt, 1, novo_nome, -1, SQLITE_TRANSIENT);
    sqlite3_bind_text(stmt, 2, novo_email, -1, SQLITE_TRANSIENT);
    sqlite3_bind_text(stmt, 3, nova_senha, -1, SQLITE_TRANSIENT);
    sqlite3_bind_int(stmt, 4, novo_status);
    sqlite3_bind_int(stmt, 5, id);

    rc = sqlite3_step(stmt);
    sqlite3_finalize(stmt);

    return rc == SQLITE_DONE ? 0 : 1;
  }
//---------------Deletar USUARIO------------
   int deletar_usuario(sqlite3 *db, int id){
    const char * sql = "DELETE FROM USUARIO WHERE IDUSUARIO = ?;";
    sqlite3_stmt *stmt;
    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK){
        fprintf(stderr, "Erro ao preparar DELETE: %s\n", sqlite3_errmsg(db));
        return 1;
    }

    sqlite3_bind_int(stmt, 1, id);

    rc = sqlite3_step(stmt);
    sqlite3_finalize(stmt);
    return rc == SQLITE_DONE ? 0 : 1;

   }
   //---------------------CRUD USUARIO----------------------------//

   //=====================================================================//

   //----------------------CRUD CURSO----------------------------//


   //---------------Criar CURSO------------

   int inserir_curso(sqlite3 *db, const char *nome, const char *descricao, const char *turno, int anoletivo ){
    const char *sql = "INSERT INTO CURSO (NOME, DESCRICAO, TURNO, ANOLETIVO) VALUES (?, ?, ?, ?);";
    sqlite3_stmt *stmt;

    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar INSERT: %s\n", sqlite3_errmsg(db));
        return 1;
      }

      sqlite3_bind_text(stmt, 1, nome, -1, SQLITE_TRANSIENT);
      sqlite3_bind_text(stmt, 2, descricao, -1, SQLITE_TRANSIENT);
      sqlite3_bind_text(stmt, 3, turno, -1, SQLITE_TRANSIENT);
      sqlite3_bind_int(stmt, 4, anoletivo);

      rc = sqlite3_step(stmt);
      sqlite3_finalize(stmt);

      return rc == SQLITE_DONE ? 0 : 1;
   }

   //---------------Listar CURSO------------
    int listar_curso(sqlite3 *db) {
      const char *sql = "SELECT IDCURSO, NOME, DESCRICAO, TURNO, ANOLETIVO FROM CURSO;";

      sqlite3_stmt *stmt;
      int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
      if (rc != SQLITE_OK) {
          fprintf(stderr, "Erro ao preparar SELECT: %s\n", sqlite3_errmsg(db));
          return 1;
      }

      printf("Lista de cursos:\n");
      while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
          printf("ID: %d | Nome: %s | Descricao: %s | Turno: %s | Ano Letivo: %d\n",
                sqlite3_column_int(stmt, 0),
                sqlite3_column_text(stmt, 1),
                sqlite3_column_text(stmt, 2),
                sqlite3_column_text(stmt, 3),
                sqlite3_column_int(stmt, 4));
      }
      sqlite3_finalize(stmt);
      return 0;
    }
    //---------------Atualizar CURSO------------

    int atualizar_curso(sqlite3 *db, const char *novo_nome_curso, const char *nova_descricao, const char *novo_turno, int novo_anoletivo, int id_curso){
      const char *sql = "UPDATE CURSO SET NOME = ?, DESCRICAO = ?, TURNO = ?, ANOLETIVO = ? WHERE IDCURSO = ?;";
      sqlite3_stmt *stmt;

      int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
      if (rc != SQLITE_OK) {
          fprintf(stderr, "Erro ao preparar UPDATE: %s\n", sqlite3_errmsg(db));
          return 1;
      }

      sqlite3_bind_text(stmt, 1, novo_nome_curso, -1, SQLITE_TRANSIENT);
      sqlite3_bind_text(stmt, 2, nova_descricao, -1, SQLITE_TRANSIENT);
      sqlite3_bind_text(stmt, 3, novo_turno, -1, SQLITE_TRANSIENT);
      sqlite3_bind_int(stmt, 4, novo_anoletivo);
      sqlite3_bind_int(stmt, 5, id_curso);

      rc = sqlite3_step(stmt);
      sqlite3_finalize(stmt);
      return rc == SQLITE_DONE ? 0 : 1;
}

  //-------------Deletar Curso------------

  int deletar_curso(sqlite3 *db, int id_curso){
    const char * sql = "DELETE FROM CURSO WHERE IDCURSO = ?;";
    sqlite3_stmt *stmt;
    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK){
        fprintf(stderr, "Erro ao preparar DELETE: %s\n", sqlite3_errmsg(db));
        return 1;
    }

    sqlite3_bind_int(stmt, 1, id_curso);

    rc = sqlite3_step(stmt);
    sqlite3_finalize(stmt);
    return rc == SQLITE_DONE ? 0 : 1;

   }

  //---------------------CRUD CURSO----------------------------//

  //=====================================================================//

   //----------------------CRUD ALUNO----------------------------//

    //---------------Criar ALUNO------------
    int inserir_aluno(sqlite3 *db, const char *RA, const char *dtnascimento, int cpf, const char *email, int telefone, int status){
      const char *sql = "INSERT INTO ALUNO (RA, DTNASCIMENTO, CPF, EMAIL, TELEFONE, STATUS) VALUES (?, ?, ?, ?, ?, ?);";
      sqlite3_stmt *stmt;

    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
      if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar INSERT: %s\n", sqlite3_errmsg(db));
        return 1;
      }

    sqlite3_bind_text(stmt, 1, RA, -1, SQLITE_TRANSIENT);
    sqlite3_bind_text(stmt, 2, dtnascimento, -1, SQLITE_TRANSIENT);
    sqlite3_bind_int(stmt, 3, cpf);
    sqlite3_bind_text(stmt, 4, email, -1, SQLITE_TRANSIENT);
    sqlite3_bind_int(stmt, 5, telefone);
    sqlite3_bind_int(stmt, 6, status);

    rc = sqlite3_step(stmt);
    sqlite3_finalize(stmt);

    return rc == SQLITE_DONE ? 0 : 1;

  }
  //----------------------Listar ALUNO-----------
  int listar_aluno(sqlite3 *db) {
    const char *sql = "SELECT RA, DTNASCIMENTO, CPF, EMAIL, TELEFONE, STATUS FROM ALUNO;";

    sqlite3_stmt *stmt;
    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
      if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar SELECT: %s\n", sqlite3_errmsg(db));
        return 1;
      }

      printf("Lista de alunos:\n");
      while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
        printf("RA: %s | Nascimento: %s | CPF: %d | Email: %s | Telefone: %d | Status: %d\n",
        sqlite3_column_text(stmt, 0),
        sqlite3_column_text(stmt, 1),
        sqlite3_column_int(stmt, 2),
        sqlite3_column_text(stmt, 3),
        sqlite3_column_int(stmt, 4),
        sqlite3_column_int(stmt, 5)
      );
      }
      sqlite3_finalize(stmt);
      return 0;
    }
//----------Atualizar ALUNO---------------

int atualizar_aluno(sqlite3 *db, const char *RA, const char *novo_dtnascimento,int novo_cpf, const char *novo_email, int novo_telefone,int novo_status) {
    const char *sql = "UPDATE ALUNO SET DTNASCIMENTO = ?, CPF = ?, EMAIL = ?, TELEFONE = ?, STATUS = ? WHERE RA = ?;";
    sqlite3_stmt *stmt;
    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar UPDATE: %s\n", sqlite3_errmsg(db));
        return 1;
    }

    sqlite3_bind_text(stmt, 1, novo_dtnascimento, -1, SQLITE_TRANSIENT);
    sqlite3_bind_int(stmt, 2, novo_cpf);
    sqlite3_bind_text(stmt, 3, novo_email, -1, SQLITE_TRANSIENT);
    sqlite3_bind_int(stmt, 4, novo_telefone);
    sqlite3_bind_int(stmt, 5, novo_status);
    sqlite3_bind_text(stmt, 6, RA, -1, SQLITE_TRANSIENT);

    rc = sqlite3_step(stmt);
    sqlite3_finalize(stmt);

    return rc == SQLITE_DONE ? 0 : 1;
}
//------------Deletar ALUNO---------------
int deletar_aluno(sqlite3 *db, const char *RA){
  const char * sql = "DELETE FROM ALUNO WHERE RA = ?;";
  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db, sql , -1, &stmt, NULL);
  if (rc !=SQLITE_OK){
    fprintf(stderr, "Erro ao prepara DELETE: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_text(stmt, 1, RA, -1, SQLITE_TRANSIENT);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);
  return rc == SQLITE_DONE ? 0 : 1;
}
//-------------------------CRUD ALUNOS--------------------//

//======================================================================//

//------------------------CRUD AULA---------------------//
//------------Criar AULA--------------
int inserir_aula(sqlite3 *db, const char *dtaula, const char *horario, const char *obs){
  const char *sql = "INSERT INTO AULA (DTAULA, HORARIO, OBS) VALUES (?, ?, ?);";
  sqlite3_stmt *stmt;

  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
  if (rc != SQLITE_OK) {
    fprintf(stderr, "Erro ao preparar INSERT: %s\n", sqlite3_errmsg(db));
    return 1;
  }
  
  sqlite3_bind_text(stmt, 1, dtaula, -1, SQLITE_TRANSIENT);
  sqlite3_bind_text(stmt, 2, horario, -1, SQLITE_TRANSIENT);
  sqlite3_bind_text(stmt, 3, obs, -1, SQLITE_TRANSIENT);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);

  return rc == SQLITE_DONE ? 0 : 1;
}
//------------Listar AULA--------------
int listar_aula(sqlite3 *db) {
  const char *sql = "SELECT IDAULA, DTAULA, HORARIO, OBS FROM AULA;";

  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
      fprintf(stderr, "Erro ao preparar SELECT: %s\n", sqlite3_errmsg(db));
      return 1;
    }

    printf("Lista de aulas:\n");
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
      printf("ID: %d | Data: %s | Horario: %s | Obs: %s\n",
      sqlite3_column_int(stmt, 0),
      sqlite3_column_text(stmt, 1),
      sqlite3_column_text(stmt, 2),
      sqlite3_column_text(stmt, 3)
      );
    }
    sqlite3_finalize(stmt);
    return 0;
}
//------------Atualizar AULA--------------
int atualizar_aula(sqlite3 *db, int idaula, const char *novo_dtaula, const char *novo_horario, const char *nova_obs) {
  const char *sql = "UPDATE AULA SET DTAULA = ?, HORARIO = ?, OBS = ? WHERE IDAULA = ?;";
  sqlite3_stmt *stmt;

    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
      if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar UPDATE: %s\n", sqlite3_errmsg(db));
        return 1;
      }

      sqlite3_bind_text(stmt, 1, novo_dtaula, -1, SQLITE_TRANSIENT);
      sqlite3_bind_text(stmt, 2, novo_horario, -1, SQLITE_TRANSIENT);
      sqlite3_bind_text(stmt, 3, nova_obs, -1, SQLITE_TRANSIENT);
      sqlite3_bind_int(stmt, 4, idaula);

      rc = sqlite3_step(stmt);
      sqlite3_finalize(stmt);

      return rc == SQLITE_DONE ? 0 : 1; 
}
//------------Deletar AULA--------------
int deletar_aula(sqlite3 *db, int idaula){
  const char * sql = "DELETE FROM AULA WHERE IDAULA = ?;";
  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db, sql , -1, &stmt, NULL);
  if (rc !=SQLITE_OK){
    fprintf(stderr, "Erro ao prepara DELETE: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_int(stmt, 1, idaula);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);
  return rc == SQLITE_DONE ? 0 : 1;
}
//-------------------------CRUD AULA--------------------//

//======================================================================//

//------------------------CRUD DISCIPLINA---------------------//

//------------Criar DISCIPLINA--------------
int inserir_disciplina(sqlite3 *db, const char *nomedisciplina, int cargahoraria){
  const char *sql = "INSERT INTO DISCIPLINA (NOMEDISCIPLINA, CARGAHORARIA) VALUES (?, ?);";
  sqlite3_stmt *stmt;

  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
  if (rc != SQLITE_OK) {
    fprintf(stderr, "Erro ao preparar INSERT: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_text(stmt, 1, nomedisciplina, -1, SQLITE_TRANSIENT);
  sqlite3_bind_int(stmt, 2, cargahoraria);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);

  return rc == SQLITE_DONE ? 0 : 1;
}
//------------Listar DISCIPLINA--------------
int listar_disciplina(sqlite3 *db) {
  const char *sql = "SELECT IDDISCIPLINA, NOMEDISCIPLINA, CARGAHORARIA FROM DISCIPLINA;";

  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
      fprintf(stderr, "Erro ao preparar SELECT: %s\n", sqlite3_errmsg(db));
      return 1;
    }

    printf("Lista de disciplinas:\n");
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
      printf("ID: %d | Nome: %s | Carga Horaria: %d\n",
      sqlite3_column_int(stmt, 0),
      sqlite3_column_text(stmt, 1),
      sqlite3_column_int(stmt, 2)
      );
    }
    sqlite3_finalize(stmt);
    return 0;
}
//------------Atualizar DISCIPLINA--------------
int atualizar_disciplina(sqlite3 *db, int iddisciplina, const char *novo_nome, int nova_carga_horaria) {
  const char *sql = "UPDATE DISCIPLINA SET NOMEDISCIPLINA = ?, CARGAHORARIA = ? WHERE IDDISCIPLINA = ?;";
  sqlite3_stmt *stmt;

    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
      if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar UPDATE: %s\n", sqlite3_errmsg(db));
        return 1;
      }

      sqlite3_bind_text(stmt, 1, novo_nome, -1, SQLITE_TRANSIENT);
      sqlite3_bind_int(stmt, 2, nova_carga_horaria);
      sqlite3_bind_int(stmt, 3, iddisciplina);

      rc = sqlite3_step(stmt);
      sqlite3_finalize(stmt);

      return rc == SQLITE_DONE ? 0 : 1; 
}
//------------Deletar DISCIPLINA--------------
int deletar_disciplina(sqlite3 *db, int iddisciplina){
  const char * sql = "DELETE FROM DISCIPLINA WHERE IDDISCIPLINA = ?;";
  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db , sql , -1, &stmt, NULL);
  if (rc !=SQLITE_OK){
    fprintf(stderr, "Erro ao prepara DELETE: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_int(stmt, 1, iddisciplina);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);
  return rc == SQLITE_DONE ? 0 : 1;
}
//-------------------------CRUD DISCIPLINA--------------------//

//======================================================================//

//------------------------CRUD PROFESSOR---------------------//

//------------Criar PROFESSOR--------------
int inserir_professor(sqlite3 *db, int cpf, const char *dtnascimento, const char *email, int telefone, const char *dtadmissao, int status){
  const char *sql = "INSERT INTO PROFESSOR (CPF, DTNASCIMENTO, EMAIL, TELEFONE, DTADMISSAO, STATUS) VALUES (?, ?, ?, ?, ?, ?);";
  sqlite3_stmt *stmt;

  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
  if (rc != SQLITE_OK) {
    fprintf(stderr, "Erro ao preparar INSERT: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_int(stmt, 1, cpf);
  sqlite3_bind_text(stmt, 2, dtnascimento, -1, SQLITE_TRANSIENT);
  sqlite3_bind_text(stmt, 3, email, -1, SQLITE_TRANSIENT);
  sqlite3_bind_int(stmt, 4, telefone);
  sqlite3_bind_text(stmt, 5, dtadmissao, -1, SQLITE_TRANSIENT);
  sqlite3_bind_int(stmt, 6, status);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);

  return rc == SQLITE_DONE ? 0 : 1;
}
//------------Listar PROFESSOR--------------
int listar_professor(sqlite3 *db) {
  const char *sql = "SELECT IDPROFESSOR, CPF, DTNASCIMENTO, EMAIL, TELEFONE, DTADMISSAO, STATUS FROM PROFESSOR;";

  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
      fprintf(stderr, "Erro ao preparar SELECT: %s\n", sqlite3_errmsg(db));
      return 1;
    }

    printf("Lista de professores:\n");
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
      printf("ID: %d | CPF: %d | Nascimento: %s | Email: %s | Telefone: %d | Admissao: %s | Status: %d\n",
      sqlite3_column_int(stmt, 0),
      sqlite3_column_int(stmt, 1),
      sqlite3_column_text(stmt, 2),
      sqlite3_column_text(stmt, 3),
      sqlite3_column_int(stmt, 4),
      sqlite3_column_text(stmt, 5),
      sqlite3_column_int(stmt, 6)
      );
    }
    sqlite3_finalize(stmt);
    return 0;
}
//------------Atualizar PROFESSOR--------------
int atualizar_professor(sqlite3 *db, int idprofessor, int novo_cpf, const char *novo_dtnascimento, const char *novo_email, int novo_telefone, const char *novo_dtadmissao, int novo_status) {
  const char *sql = "UPDATE PROFESSOR SET CPF = ?, DTNASCIMENTO = ?, EMAIL = ?, TELEFONE = ?, DTADMISSAO = ?, STATUS = ? WHERE IDPROFESSOR = ?;";
  sqlite3_stmt *stmt;

    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
      if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar UPDATE: %s\n", sqlite3_errmsg(db));
        return 1;
      }

      sqlite3_bind_int(stmt, 1, novo_cpf);
      sqlite3_bind_text(stmt, 2, novo_dtnascimento, -1, SQLITE_TRANSIENT);
      sqlite3_bind_text(stmt, 3, novo_email, -1, SQLITE_TRANSIENT);
      sqlite3_bind_int(stmt, 4, novo_telefone);
      sqlite3_bind_text(stmt, 5, novo_dtadmissao, -1, SQLITE_TRANSIENT);
      sqlite3_bind_int(stmt, 6, novo_status);
      sqlite3_bind_int(stmt, 7, idprofessor);

      rc = sqlite3_step(stmt);
      sqlite3_finalize(stmt);

      return rc == SQLITE_DONE ? 0 : 1; 
}
//------------Deletar PROFESSOR--------------
int deletar_professor(sqlite3 *db, int idprofessor){
  const char * sql = "DELETE FROM PROFESSOR WHERE IDPROFESSOR = ?;";
  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db , sql , -1, &stmt, NULL);
  if (rc !=SQLITE_OK){
    fprintf(stderr, "Erro ao prepara DELETE: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_int(stmt, 1, idprofessor);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);
  return rc == SQLITE_DONE ? 0 : 1;
}

//-------------------------CRUD PROFESSOR--------------------//

//======================================================================//

//-------------------------CRUD ENTREGA EXERCICIO--------------------//

//------------Criar ENTREGA EXERCICIO--------------
int inserir_entrega_exercicio(sqlite3 *db, const char *dtenvio, const char *arquivo, const char *ra, int notaexercicio){
  const char *sql = "INSERT INTO ENTREGAEXERCICIO (DTENVIO, ARQUIVO, RA, NOTAEXERCICIO) VALUES (?, ?, ?, ?);";
  sqlite3_stmt *stmt;

  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
  if (rc != SQLITE_OK) {
    fprintf(stderr, "Erro ao preparar INSERT: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_text(stmt, 1, dtenvio, -1, SQLITE_TRANSIENT);
  sqlite3_bind_text(stmt, 2, arquivo, -1, SQLITE_TRANSIENT);
  sqlite3_bind_text(stmt, 3, ra, -1, SQLITE_TRANSIENT);
  sqlite3_bind_int(stmt, 4, notaexercicio);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);

  return rc == SQLITE_DONE ? 0 : 1;
}

//------------Listar ENTREGA EXERCICIO--------------
int listar_entrega_exercicio(sqlite3 *db) {
  const char *sql = "SELECT IDENTREGA, DTENVIO, ARQUIVO, NOTAEXERCICIO, RA FROM ENTREGAEXERCICIO;";

  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
      fprintf(stderr, "Erro ao preparar SELECT: %s\n", sqlite3_errmsg(db));
      return 1;
    }

    printf("Lista de entregas de exercicios:\n");
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
      printf("ID: %d | Data Envio: %s | Arquivo: %s | Nota: %d | RA: %s\n",
      sqlite3_column_int(stmt, 0),
      sqlite3_column_text(stmt, 1),
      sqlite3_column_text(stmt, 2),
      sqlite3_column_int(stmt, 3),
      sqlite3_column_text(stmt, 4)
      );
    }
    sqlite3_finalize(stmt);
    return 0;
}
//------------Atualizar ENTREGA EXERCICIO--------------
int atualizar_entrega_exercicio(sqlite3 *db, int identrega, const char *novo_dtenvio, const char *novo_arquivo, int novo_notaexercicio, const char *novo_ra) {
  const char *sql = "UPDATE ENTREGAEXERCICIO SET DTENVIO = ?, ARQUIVO = ?, NOTAEXERCICIO = ?, RA = ? WHERE IDENTREGA = ?;";
  sqlite3_stmt *stmt;

    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
      if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar UPDATE: %s\n", sqlite3_errmsg(db));
        return 1;
      }

      sqlite3_bind_text(stmt, 1, novo_dtenvio, -1, SQLITE_TRANSIENT);
      sqlite3_bind_text(stmt, 2, novo_arquivo, -1, SQLITE_TRANSIENT);
      sqlite3_bind_int(stmt, 3, novo_notaexercicio);
      sqlite3_bind_text(stmt, 4, novo_ra, -1, SQLITE_TRANSIENT);
      sqlite3_bind_int(stmt, 5, identrega);

      rc = sqlite3_step(stmt);
      sqlite3_finalize(stmt);

      return rc == SQLITE_DONE ? 0 : 1; 
}
//------------Deletar ENTREGA EXERCICIO--------------
int deletar_entrega_exercicio(sqlite3 *db, int identrega){
  const char * sql = "DELETE FROM ENTREGAEXERCICIO WHERE IDENTREGA = ?;";
  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db , sql , -1, &stmt, NULL);
  if (rc !=SQLITE_OK){
    fprintf(stderr, "Erro ao prepara DELETE: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_int(stmt, 1, identrega);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);
  return rc == SQLITE_DONE ? 0 : 1;
}

//-------------------------CRUD ENTREGA EXERCICIO--------------------//

//======================================================================//

//-------------------------CRUD EXERCICIO---------------------//
//------------Criar EXERCICIO--------------
int inserir_exercicio(sqlite3 *db, const char *titulo, const char *descricao, const char *dtentrega){
  const char *sql = "INSERT INTO EXERCICIO (TITULO, DESCRICAO, DTENTREGA) VALUES (?, ?, ?);";
  sqlite3_stmt *stmt;

  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
  if (rc != SQLITE_OK) {
    fprintf(stderr, "Erro ao preparar INSERT: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_text(stmt, 1, titulo, -1, SQLITE_TRANSIENT);
  sqlite3_bind_text(stmt, 2, descricao, -1, SQLITE_TRANSIENT);
  sqlite3_bind_text(stmt, 3, dtentrega, -1, SQLITE_TRANSIENT);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);

  return rc == SQLITE_DONE ? 0 : 1;
}
//------------Listar EXERCICIO--------------
int listar_exercicio(sqlite3 *db) {
  const char *sql = "SELECT IDEXERCICIO, TITULO, DESCRICAO, DTENTREGA FROM EXERCICIO;";

  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
      fprintf(stderr, "Erro ao preparar SELECT: %s\n", sqlite3_errmsg(db));
      return 1;
    }

    printf("Lista de exercicios:\n");
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
      printf("ID: %d | Titulo: %s | Descricao: %s | Data Entrega: %s\n",
      sqlite3_column_int(stmt, 0),
      sqlite3_column_text(stmt, 1),
      sqlite3_column_text(stmt, 2),
      sqlite3_column_text(stmt, 3)
      );
    }
    sqlite3_finalize(stmt);
    return 0;
}
//------------Atualizar EXERCICIO--------------
int atualizar_exercicio(sqlite3 *db, int idexercicio, const char *novo_titulo, const char *nova_descricao, const char *nova_dtentrega) {
  const char *sql = "UPDATE EXERCICIO SET TITULO = ?, DESCRICAO = ?, DTENTREGA = ? WHERE IDEXERCICIO = ?;";
  sqlite3_stmt *stmt;

    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
      if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar UPDATE: %s\n", sqlite3_errmsg(db));
        return 1;
      }

      sqlite3_bind_text(stmt, 1, novo_titulo, -1, SQLITE_TRANSIENT);
      sqlite3_bind_text(stmt, 2, nova_descricao, -1, SQLITE_TRANSIENT);
      sqlite3_bind_text(stmt, 3, nova_dtentrega, -1, SQLITE_TRANSIENT);
      sqlite3_bind_int(stmt, 4, idexercicio);

      rc = sqlite3_step(stmt);
      sqlite3_finalize(stmt);

      return rc == SQLITE_DONE ? 0 : 1;
}
//------------Deletar EXERCICIO--------------
int deletar_exercicio(sqlite3 *db, int idexercicio){
  const char * sql = "DELETE FROM EXERCICIO WHERE IDEXERCICIO = ?;";
  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db , sql , -1, &stmt, NULL);
  if (rc !=SQLITE_OK){
    fprintf(stderr, "Erro ao prepara DELETE: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_int(stmt, 1, idexercicio);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);
  return rc == SQLITE_DONE ? 0 : 1;
}

//-------------------------CRUD EXERCICIO--------------------//

//======================================================================//

//-------------------------CRUD FREQUENCIA---------------------//

//------------Criar FREQUENCIA--------------
int inserir_frequencia(sqlite3 *db, int presenca, const char *ra){
  const char *sql = "INSERT INTO FREQUENCIA (PRESENCA, RA) VALUES (?, ?);";
  sqlite3_stmt *stmt;

  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
  if (rc != SQLITE_OK) {
    fprintf(stderr, "Erro ao preparar INSERT: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_int(stmt, 1, presenca);
  sqlite3_bind_text(stmt, 2, ra, -1, SQLITE_TRANSIENT);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);

  return rc == SQLITE_DONE ? 0 : 1;
}
//------------Listar FREQUENCIA--------------
int listar_frequencia(sqlite3 *db) {
  const char *sql = "SELECT IDFREQUENCIA, PRESENCA, RA FROM FREQUENCIA;";

  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
      fprintf(stderr, "Erro ao preparar SELECT: %s\n", sqlite3_errmsg(db));
      return 1;
    }

    printf("Lista de frequencias:\n");
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
      printf("ID: %d | Presenca: %d | RA: %s\n",
      sqlite3_column_int(stmt, 0),
      sqlite3_column_int(stmt, 1),
      sqlite3_column_text(stmt, 2)
      );
    }
    sqlite3_finalize(stmt);
    return 0;
}
//------------Atualizar FREQUENCIA--------------
int atualizar_frequencia(sqlite3 *db, int idfrequencia, int nova_presenca, const char *novo_ra) {
  const char *sql = "UPDATE FREQUENCIA SET PRESENCA = ?, RA = ? WHERE IDFREQUENCIA = ?;";
  sqlite3_stmt *stmt;

    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
      if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar UPDATE: %s\n", sqlite3_errmsg(db));
        return 1;
      }

      sqlite3_bind_int(stmt, 1, nova_presenca);
      sqlite3_bind_text(stmt, 2, novo_ra, -1, SQLITE_TRANSIENT);
      sqlite3_bind_int(stmt, 3, idfrequencia);

      rc = sqlite3_step(stmt);
      sqlite3_finalize(stmt);

      return rc == SQLITE_DONE ? 0 : 1; 
}
//------------Deletar FREQUENCIA--------------
int deletar_frequencia(sqlite3 *db, int idfrequencia){
  const char * sql = "DELETE FROM FREQUENCIA WHERE IDFREQUENCIA = ?;";
  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db , sql , -1, &stmt, NULL);
  if (rc !=SQLITE_OK){
    fprintf(stderr, "Erro ao prepara DELETE: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_int(stmt, 1, idfrequencia);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);
  return rc == SQLITE_DONE ? 0 : 1;
}

//-------------------------CRUD FREQUENCIA--------------------//

//======================================================================//

//-------------------------CRUD NOTA---------------------//

//------------Criar NOTA--------------
int inserir_nota(sqlite3 *db, int valor, const char *tipoavaliacao, const char *ra){
  const char *sql = "INSERT INTO NOTA (VALOR, TIPOAVALIACAO, RA) VALUES (?, ?, ?);";
  sqlite3_stmt *stmt;

  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
  if (rc != SQLITE_OK) {
    fprintf(stderr, "Erro ao preparar INSERT: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_int(stmt, 1, valor);
  sqlite3_bind_text(stmt, 2, tipoavaliacao, -1, SQLITE_TRANSIENT);
  sqlite3_bind_text(stmt, 3, ra, -1, SQLITE_TRANSIENT);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);

  return rc == SQLITE_DONE ? 0 : 1;
}
//------------Listar NOTA--------------
int listar_nota(sqlite3 *db) {
  const char *sql = "SELECT IDNOTA, VALOR, TIPOAVALIACAO, RA FROM NOTA;";

  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
      fprintf(stderr, "Erro ao preparar SELECT: %s\n", sqlite3_errmsg(db));
      return 1;
    }

    printf("Lista de notas:\n");
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
      printf("ID: %d | Valor: %d | Tipo Avaliacao: %s | RA: %s\n",
      sqlite3_column_int(stmt, 0),
      sqlite3_column_int(stmt, 1),
      sqlite3_column_text(stmt, 2),
      sqlite3_column_text(stmt, 3)
      );
    }
    sqlite3_finalize(stmt);
    return 0;
}
//------------Atualizar NOTA--------------
int atualizar_nota(sqlite3 *db, int idnota, int novo_valor, const char *novo_tipoavaliacao, const char *novo_ra) {
  const char *sql = "UPDATE NOTA SET VALOR = ?, TIPOAVALIACAO = ?, RA = ? WHERE IDNOTA = ?;";
  sqlite3_stmt *stmt;

    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
      if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar UPDATE: %s\n", sqlite3_errmsg(db));
        return 1;
      }

      sqlite3_bind_int(stmt, 1, novo_valor);
      sqlite3_bind_text(stmt, 2, novo_tipoavaliacao, -1, SQLITE_TRANSIENT);
      sqlite3_bind_text(stmt, 3, novo_ra, -1, SQLITE_TRANSIENT);
      sqlite3_bind_int(stmt, 4, idnota);

      rc = sqlite3_step(stmt);
      sqlite3_finalize(stmt);

      return rc == SQLITE_DONE ? 0 : 1; 
}
//------------Deletar NOTA--------------
int deletar_nota(sqlite3 *db, int idnota){
  const char * sql = "DELETE FROM NOTA WHERE IDNOTA = ?;";
  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db , sql , -1, &stmt, NULL);
  if (rc !=SQLITE_OK){
    fprintf(stderr, "Erro ao prepara DELETE: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_int(stmt, 1, idnota);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);
  return rc == SQLITE_DONE ? 0 : 1;
}
//-------------------------CRUD NOTA--------------------//

//======================================================================//

//-------------------------CRUD SALA---------------------//
//------------Criar SALA--------------
int inserir_sala(sqlite3 *db, const char *nome_sala){
  const char *sql = "INSERT INTO SALA (NOME) VALUES (?);";
  sqlite3_stmt *stmt;

  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
  if (rc != SQLITE_OK) {
    fprintf(stderr, "Erro ao preparar INSERT: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_text(stmt, 1, nome_sala, -1, SQLITE_TRANSIENT);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt); 

  return rc == SQLITE_DONE ? 0 : 1;
}
//------------Listar SALA--------------
int listar_sala(sqlite3 *db) {
  const char *sql = "SELECT IDSALA, NOME FROM SALA;";

  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
      fprintf(stderr, "Erro ao preparar SELECT: %s\n", sqlite3_errmsg(db));
      return 1;
    }

    printf("Lista de salas:\n");
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
      printf("ID: %d | Nome: %s\n",
      sqlite3_column_int(stmt, 0),
      sqlite3_column_text(stmt, 1)
      );
    }
    sqlite3_finalize(stmt);
    return 0;
}
//------------Atualizar SALA--------------
int atualizar_sala(sqlite3 *db, int idsala, const char *novo_nome) {
  const char *sql = "UPDATE SALA SET NOME = ? WHERE IDSALA = ?;";
  sqlite3_stmt *stmt;

    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
      if (rc != SQLITE_OK) {
        fprintf(stderr, "Erro ao preparar UPDATE: %s\n", sqlite3_errmsg(db));
        return 1;
      }

      sqlite3_bind_text(stmt, 1, novo_nome, -1, SQLITE_TRANSIENT);
      sqlite3_bind_int(stmt, 2, idsala);

      rc = sqlite3_step(stmt);
      sqlite3_finalize(stmt);

      return rc == SQLITE_DONE ? 0 : 1; 
}
//------------Deletar SALA--------------
int deletar_sala(sqlite3 *db, int idsala){
  const char * sql = "DELETE FROM SALA WHERE IDSALA = ?;";
  sqlite3_stmt *stmt;
  int rc = sqlite3_prepare_v2(db , sql , -1, &stmt, NULL);
  if (rc !=SQLITE_OK){
    fprintf(stderr, "Erro ao prepara DELETE: %s\n", sqlite3_errmsg(db));
    return 1;
  }

  sqlite3_bind_int(stmt, 1, idsala);

  rc = sqlite3_step(stmt);
  sqlite3_finalize(stmt);
  return rc == SQLITE_DONE ? 0 : 1;
}
//-------------------------CRUD SALA--------------------//

//======================================================================//