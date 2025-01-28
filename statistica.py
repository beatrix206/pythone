voti = []

for i in range(10):
    valutazione =  input ()
    voti.append(int(valutazione))
voti.remove(min(voti))
voti.remove(max(voti))
print("la media dei voti è:" , (sum(voti)/len(voti)) )