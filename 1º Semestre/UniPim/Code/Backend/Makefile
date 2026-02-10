CC = gcc
CFLAGS = -Wall -I. -I./routes -I./utils -I./config
LDFLAGS = -lpthread

OBJS = main.o routes/alunos.o routes/professores.o utils/response.o

all: erp_api

erp_api: $(OBJS)
	$(CC) -o erp_api $(OBJS) $(LDFLAGS)

clean:
	rm -f $(OBJS) erp_api
