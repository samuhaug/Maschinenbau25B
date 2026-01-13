Temperatur = int(input("Geben Sie die Temperatur ein!"))
zu_kalt = (Temperatur < 20)
zu_warm = (Temperatur > 80)
ist_in_ordnung = not(zu_kalt or zu_warm)

print("Die Temperatur ist in Ordnung:", zu_kalt, zu_warm, ist_in_ordnung)