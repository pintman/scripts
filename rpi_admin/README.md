
# RPi-Admin

Mit Hilfe von [Ansible](https://www.ansible.com) lässt sich eine Sammlung von
Raspberry Pis fernsteuern.

Das Repo enhält eine Datei ``hosts.example``, die als Vorlage dient. Sie kann
für die eigenen Versuche nach ``hosts`` kopiert und angepasst werden. In ihr
sind alle Rechner eingetragen, die administriert werden sollen.

## Vorbereitung

### Hosts ermitteln

Zunächst müssen die Clients ermitteln und in der Datei ``hosts`` abgelegt
werden. Dort können z.B. auch Gruppen für jeden Raum erstellt werden. Mit nmap
können die Clients im lokalen Netz schnell ermittelt werden, wenn die
Hostnamen nicht bekannt sind:

    $ nmap -sP -n 192.168.178.0/24

### SSH-Server installieren

Da die Administration über SSH läuft, muss ein OpenSSH-Server auf jedem Client
installiert und gestartet werden.

Dann werden die öffentlichen SSH-Keys auf jeden Client aus der ``hosts``-Datei
übertragen - z.B. mit folgendem Aufruf:

    $ ssh-copy-id 192.168.178.21
    $ ssh-copy-id 192.168.178.22
    $ ssh-copy-id 192.168.178.23

## Aufruf

Die Datei ``setup.yml`` enthält ein sogenanntes
[Playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html), mit dem die
Rechner vorbereitet werden.

Ein typischer Aufruf wäre 

    $ ansible-playbook -i hosts setup.yml

Nach einer Klassenarbeit können Abgagen mit dem Playbook
``abgaben_einsammeln.yml`` eingesammelt werden.

    $ ansible-playbook -i hosts abgaben_einsammeln.yml
    
Die Abgabe muss auf jedem Client in einer speziellen Datei abgelegt werden.
