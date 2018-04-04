class Arma:        
    def __repr__(self):
        return self.nome

  
class Pugnale(Arma):
    def __init__(self):
        self.name = "Pugnale"
        self.description = "Un pugnale dall'aspetto grezzo."
        self.damage = 5

class Ascia(Arma):
	def __init__(self):
		self.nome = "Ascia"
		self.descrizione = "Una scintillante ascia costruita di metallo nero."
		self.danno = 15


mioinventario = ['Pugnale()','Oro(10)','Mela']
print("La mia prima avventura di testo con procedure di movimento")
print ("Sei in una stanza fiocamente illuminata. A ovest c'è una porta. Di fronte a te c'è un tavolo. Sul tavolo c'è un'ascia.")

def muovi_giocatore():
    return input("Cosa fai? ")
    
action = muovi_giocatore()

if action == "vai a ovest":
	print("La porta è bloccata.")
elif action == "vai a sud":
    print("Non puoi andare in quella direzione.")
elif action == "vai a est":
    print("Non puoi andare in quella direzione.")
elif action == "vai a nord":
    print("Non puoi andare in quella direzione.")
elif action == "prendi ascia":
    print("Hai preso l'ascia.")
    mioinventario.append("Ascia()")
elif action == "i":
    print(mioinventario)
else:
    print("Non puoi farlo.")