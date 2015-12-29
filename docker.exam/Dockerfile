# From https://docs.docker.com/engine/examples/running_ssh_service/
#
# Docker-Container für den Einsatz in Klassenarbeiten. 
#
# Der Container kann gebaut werden mit
#
# docker build -t exam .
#
# Anschließend kann er gestartet werden mit
#
# docker run -p 22 -p 80 -p 443 exam
#
# Die vergebenen Ports können anschließend mit 'docker ps' ermitteln
# werden. Die Ports auch händisch gemapped werden:
#
# docker run -p 50022:22 -p 50080:80 -p docker 50443:443 exam
#
# Ein Schwung Container wird einfach gestartet mit
#
# for i in $(seq 3); do docker run -d --name=exam$i -p 22 -p 80 exam; done
#
# Beendet und entfernt werden sie wieder mit
#
# for i in $(seq 3); do docker stop exam$i; done
# for i in $(seq 3); do docker rm exam$i; done
#
# VERSION               0.0.4

FROM ubuntu:14.04
MAINTAINER Marco Bakera <marco@bakera.de>

# Testuser anlegen und Passwörter setzen
RUN useradd -s /bin/bash -m testuser
RUN echo 'testuser:wohnzimmer' | chpasswd
RUN echo 'root:wohnzimmer' | chpasswd

# sudo für neuen User aktivieren
RUN echo 'testuser ALL=(ALL:ALL) ALL' >> /etc/sudoers

# Pakete installieren
RUN apt-get update && apt-get install -y \
  apache2 \
  libapache2-mod-php5 \
  man \
  nano \
  openssh-server \
  wget \
  vim \
&& apt-get clean

# sshd konfigurieren
RUN mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# dokuwiki herunterladen
RUN wget -qP /tmp http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz
#RUN tar -C /tmp/ -xzf /tmp/dokuwiki-stable.tgz 

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# Ports verfügbar machen - SSH, HTTP(S)
EXPOSE 22 80 443

# Startskript in den Container kopieren und ausführen
COPY ./docker-entrypoint.sh /
CMD ["/docker-entrypoint.sh", ""]

