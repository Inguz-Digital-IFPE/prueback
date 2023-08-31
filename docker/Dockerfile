FROM AWSACCOUNTID.dkr.ecr.us-east-2.amazonaws.com/ECREPOSITORY:django3.9 AS whole_app

WORKDIR /prueback

COPY docker/entrypoint.sh entrypoint.sh

#Un RUN corre un comando y crea una nueva capa sobre la imagen
RUN ["chmod", "+x", "entrypoint.sh"]

#Nos dice el comando que se correrá cuando corramos la imagen
# a diferencia de CMD, que pone un comando estándar cuando no damos
# ningún argumento
# entrypoint siempre se corre al correr la imagen
ENTRYPOINT ["sh", "entrypoint.sh"]

COPY /prueback/. .
