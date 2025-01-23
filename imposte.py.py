reddito= int(input("qual'è il tuo reddito?"))
ALIQUOTA_1=0.23
ALIQUOTA_2=0.35
ALIQUOTA_3=0.43
if reddito <= 28000 :
	tasse= float(reddito*ALIQUOTA_1)
else:
	if reddito<=50000 :
		tasse=float(28000*ALIQUOTA_1 +(reddito-28000)*ALIQUOTA_2)
	else:
		if reddito >50000 :
			tasse= float (28000*ALIQUOTA_1 + (50000-28000)* ALIQUOTA_2 + (reddito - 50000)*ALIQUOTA_3)
print(tasse)
input( "termina" )