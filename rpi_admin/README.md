
# RPi-Admin

Mit Hilfe von [Ansible](http://www.ansible.com) lässt sich eine Sammlung von Raspberry Pi fernsteuern.

In der Datei ``hosts`` sind alle Rechner eingetragen, die das Inventar der Rechner repräsentieren. Hier müssen alle Rechner eingetragen werden, die verwaltet werden sollen. 

## Vorbereitung

Bevor die Rechner administriert werden können, muss ein OpenSSH-Server auf jedem Client laufen. Dann werden die privaten SSH-Keys auf jeden Client aus der ``hosts``-Datei übertragen - z.B. mit folgendem Aufruf:

    $ ssh-copy-id 192.168.178.25   

## Aufruf

Die Datei ``setup.yml`` enthält ein [Playbook](http://docs.ansible.com/ansible/playbooks.html), mit dem die Rechner vorbereitet werden.

Ein typischer Aufruf wäre 

    $ ansible-playbook -i hosts setup.yml

Nach eine Klassenarbeit können Abgagen mit dem Playbook ``abgaben_einsammeln.yml`` eingesammelt werden.

    $ ansible-playbook -i hosts abgaben_einsammeln.yml
    
Die Abgabe muss auf jedem Client in einer speziellen Datei abgelegt werden.