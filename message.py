class Message :
    def __init__(self , mittente , destinatario ) : 
                 self._mittente = mittente
                 self._destinatario = destinatario
                 self._corpoMessaggio = []
    def mittente(self) :
            return self._mittente
    def destinatario(self) : 
            return self._destinatario
   
    def append (self , riga ) :
            self._corpoMessaggio.append(riga)

    def toString (self ) :
            return "Mittente: " + self._mittente +"\nDestinatario: " + self._destinatario + "\nMessaggio:\n  " + "\n  ".join(self._corpoMessaggio)
m= Message("Maria Beatrice" , "Silvia")
m.append("ciao Silvia,")
m.append("come stai?")
m.append("Cosa fai stasera?")

print (m.toString())
