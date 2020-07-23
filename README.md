# celery-example

Antes de executar o exemplo, é necessário subir o Rabbit no docker com o comando:

$ docker run -d -p 5672:5672 rabbitmq

É necessário também instalar as bibliotecas:

pip install celery

pip install requests