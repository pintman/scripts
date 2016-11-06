
# RPi-Admin

Mit Hilfe von [Ansible](http://www.ansible.com) lässt sich eine Sammlung von Raspberry Pi fernsteuern.

In der Datei ``hosts`` sind alle Rechner eingetragen, die das Inventar der Rechner repräsentieren. Hier müssen alle Rechner eingetragen werden, die verwaltet werden sollen. 

## Vorbereitung

### Hosts ermitteln

Zunächst müssen die Clients ermitteln und in der Datei ``hosts`` abgelegt werden. Dort können z.B. auch Gruppen für jeden Raum erstellt werden. Mit nmap können die Clients im lokalen Netz schnell ermittelt werden:

    $ nmap -sP -n 192.168.178.0/24

### SSH-Server installieren

Nun muss ein OpenSSH-Server auf jedem Client installiert oder gestartet werden. Raspberry Pi mit Raspbian als OS starten bereits mit einem aufenden SSH-Server.

Dann werden die privaten SSH-Keys auf jeden Client aus der ``hosts``-Datei übertragen - z.B. mit folgendem Aufruf:

    $ ssh-copy-id 192.168.178.21
    $ ssh-copy-id 192.168.178.22   
    $ ssh-copy-id 192.168.178.23   

## Aufruf

Die Datei ``setup.yml`` enthält ein [Playbook](http://docs.ansible.com/ansible/playbooks.html), mit dem die Rechner vorbereitet werden.

Ein typischer Aufruf wäre 

    $ ansible-playbook -i hosts setup.yml

Nach eine Klassenarbeit können Abgagen mit dem Playbook ``abgaben_einsammeln.yml`` eingesammelt werden.

    $ ansible-playbook -i hosts abgaben_einsammeln.yml
    
Die Abgabe muss auf jedem Client in einer speziellen Datei abgelegt werden.