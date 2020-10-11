# message-scheduler

Uma API REST para agendamento de comunicações.

### O que foi utilizado?

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [Postgresql](https://www.postgresql.org/)

### Instalação

Dependências:
- [Docker 19.03.8 +](https://docs.docker.com/get-docker/)
- [Docker Compose 1.23.2 +](https://docs.docker.com/compose/install/)

Instalar as dependências

```sh
$ cd message-scheduler
$ make build
```

Rodar as migrações

```sh
$ make migrate
```

Rodar os tests

```sh
$ make test
```
Criar um usuário

```sh
$ make createsuperuser
```
Iniciar o projeto

```sh
$ make runserver
```
Por padrão o serviço vai rodar na porta 8000, portanto estará acessível pelo endereço:
http://localhost:8000/

O Message Scheduler usa o Django REST Framework que provêm uma [documentação interativa para a API](https://www.django-rest-framework.org/topics/documenting-your-api/#self-describing-apis)
