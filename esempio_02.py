# il programma deve chiedere un numero intero e una lettera
#in output: un albero fatto con la lettera inserita   
#    A
#   AAA
#  AAAAA

numero = int(input("dammi un nunmero"))
lettera = str(input("dammi una lettera"))
contatore = 1
for i in range (numero) :
    i = (" " * numero + lettera * contatore )
    numero -= 1
    contatore += 2
    print(i)
