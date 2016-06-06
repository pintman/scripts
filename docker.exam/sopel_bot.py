from sopel import module

@module.commands('docker_exam')
@module.require_admin("Hier dürfen nur Admins ran.")
def docker_exam(bot, trigger):
    """
    Erlaubt das Starten und Verwalten von docker-Containern.
    .docker_exam run 3 - Starte 3 Container
    .docker_exam show  - zeige laufende Container
    .docker_exam stop  - stoppt alle Container
    """
    bot.say("(noch nicht fertig)")
    
    anzahl = 0
    argumente = trigger.group(2)
    method = argumente.split(' ')[0]
    #print("method", method)
    parameter = argumente.split(' ')[1:]
    #print("parameter", parameter)
        
    #print("werte Parameter aus")
    for param in parameter:
        if method == "run" and "anzahl=" in param:
            anzahl = int(param.split('=')[1])
    
    if method == "run":
        bot.say("Starte " + str(anzahl) + " Container")

    elif method == "show":
        bot.say("Ich zeige dir die laufenden Container.")
    elif method == "stop":
        bot.say("Stoppe die laufenden Container.")
        bot.say("Hoffentlich haben alle ihren Daten vorher gesichert.")
    else:
        bot.say("Keine Ahnung, was " + method + " bedeuten soll")
    
    """    
    print("trigger:", trigger)
    print("g1", trigger.group(1))
    print("g2", trigger.group(2))
    print("g3", trigger.group(3))
    print("g4", trigger.group(3))
    """


