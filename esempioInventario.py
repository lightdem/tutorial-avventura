mioinventario = ['Pugnale','Oro(10)','Mela']
print("La mia prima avventura di testo con procedure di movimento")
print ("Sei in una stanza fiocamente illuminata. A ovest c'è una porta. Di fronte a te c'è un tavolo. Sul tavolo c'è una chiave arruginito.")

def muovi_giocatore():
    return input("Cosa fai? ")
    
action = muovi_giocatore()

if action == "vai a ovest":
	print("La porta è bloccata.")
    if mioinventario.count("chiave") == 0:
        print("Non hai la chiave.")
    else:
        print("Hai aperto la porta con la chiave.")
elif action == "vai a sud":
    print("Non puoi andare in quella direzione.")
elif action == "vai a est":
    print("Non puoi andare in quella direzione.")
elif action == "vai a nord":
    print("Non puoi andare in quella direzione.")
elif action == "prendi la chiave":
    print("Hai preso la chiave arrugginita.")
    mioinventario.append("chiave")
elif action == "i":
    print(mioinventario)
else:
    print("Non puoi farlo.")