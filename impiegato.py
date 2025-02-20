# classe Emplpyee i cui oggetti hanno un NOME, COGNOME E SALRIO
# sottoclasse Manager con una variabile di istanza addizionale per indicare il reparto gestito.
# realizzare il metodo: __repr__ che visualizzi NOME COGNOME REPARTO E SALARIO
# 
class Employee :
    def __init__(self,nome,cognome ,salario):
        self._nome = nome
        self._cognome = cognome
        self._salario = salario
    def setName(self, nome) :
        self._nome = nome
    def setSurname(self, cognome) : 
        self._cognome = cognome
    def setSalary(self, salario) :
        self._salary = salario

class Manager(Employee) :
    def __init__ (self, nome , cognome, reparto, salario) :
        super().__init__(nome,cognome,salario)
        self._topic = reparto    #variabile addizionale
    def __repr__(self) :
        return self._nome + " " + self._cognome  + " lavora nel reparto  " + self._topic + " e percepisce uno stipedio di  " + self._salario + "€"


MariaBeatrice = Manager ("MariaBeatrice" , "Bozzi" , "Banca", "2000")
print (MariaBeatrice)
