print("CNC Drehzahl Sequenzen")
for drehen_drehzahl in range (200,2001,200):
    print (drehen_drehzahl, end=" ")
print() #Zeilenumbruch
for fräsen_drehzahl in range(3000,10000,1000):
    print(fräsen_drehzahl, end=" ")
print() #Zeilenumbruch
for bohren_drehzahl in range(1000,5000,500):
    print(bohren_drehzahl, end=" ")
print() #Zeilenumbr
for hochlauf_test in range(0,1000,100):
    print(hochlauf_test, end=" ")
print() #Zeilenumbr
for notfall_abbruch in range(3000, -1, -500):
    print(notfall_abbruch, end=" ")