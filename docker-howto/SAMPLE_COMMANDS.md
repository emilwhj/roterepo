### ps
Se hvilke containere som kjører
### ps -a
Se alle kontainere
### images
Se alle images
### build
Bygger et images fra en Dockerfile
### build -t
-t anngit "taggen", navnet og versjonen på imaget
### run
Starter en kontainer fra et image
### run --rm
--rm er å slette kontaineren automatisk etter kontaineren er stanset ``docker run --rm getting-started:v1.0``
### run -it bash
start en kontainer "interaktivt", aka du kan skrive kommandoer i terminalen til kontaineren, fint for debugging.  
Merk: naven på taggen må imellom -it og bash, som dette: ``docker run -it getting-started:v1.0 bash``
### run -p
Åpner en port imellom kontaineren og din lokale datamaskin: ``docker run -p 8080:8080 getting-started:v1.0``
### run -d
Kjører kontaineren detached, dvs den kjører i bakgrunnen og du ser ikke outputten fra programmet kontaineren kjører ``docker run -d getting-started:v1.0``
### run --name
Gi et navn til kontaineren