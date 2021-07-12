# Docker tutorial

## Prerequisite
- Docker
- curl
- make

### Installer curl og make på Windows
https://chocolatey.org/install  
``choco install curl make``

## Dockerfile
``FROM python``  
Bruker python som "base image", et ferdig konfigurert opperativsystem med python3 hentet fra dockerhub
https://hub.docker.com/_/python  

``RUN pip install flask``  
Innstallerer dependencies, i main.go brukes Flask som ikke følger med i base imaget

``COPY main.py /main.py``  
Kopierer python filen inn i kontaineren

``CMD ["python", "main.py"]``  
Anngir kommandoen som skal kjøres når kontaineren starter, tilsvarer å skrive `python main.py` i terminalen

### Lag image fra Dockerfile
``docker build -t getting-started:v1.0 .``  
Denne kommandoen bruker Dockerfile til å lage et nytt container image, `-t` angir "taggen", navnet på image og versionen. Det siste tegnet i kommandoen, `.` anngir plasseringen til Dockerfilen.  
Bruker du det samme navnet og versjonen når du kjører kommandoen på nytt, vil det gamle imaget bli skrevet over. Øk versjonenr hvis du ønsker å kunne spare på gamle versioner: `-t getting-started:v1.1`.  
Du kan også la være å bruke versjonnr, da vil "latest" bli brukt.  
dvs `getting-started` er det samme som `getting-started:latest`

For å se image du nettopp har laget, skriv ``docker images``  

Start kontaineren ``docker run --name getting-started -dp 8080:8080 getting-started:v1.0``  

Sjekk at kontaineren har startet ``docker ps``

Test webserveren ``curl localhost:8080``  
Fungerer alt som det skal, vil du få ut

Stop kontaineren ``docker stop getting-started``

### Python programmet er hentet fra
https://stoplight.io/blog/python-rest-api/  
https://forums.docker.com/t/docker-curl-56-recv-failure/54172

### Les mer om Docker
https://docs.docker.com/get-started/02_our_app/