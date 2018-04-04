print ("Il gioco che non dovrebbe essere")
print ("Sei in una stanza fiocamente illuminata. A ovest c'è una porta. Di fronte a te c'è un tavolo. Sul tavolo c'è una mela.")
action = input("Cosa fai?")

if action == "vai a ovest":
    print("La porta è chiusa.")
elif action == "vai a sud":
    print("Non puoi andare in quella direzione.")
elif action == "vai a est":
    print("Non puoi andare in quella direzione.")
elif action == "vai a nord":
    print("Non puoi andare in quella direzione.")
elif action == "prendi la mela":
    print("Hai preso la mela.")