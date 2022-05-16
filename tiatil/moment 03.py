# import
# variabler
# main loop
# funktioner som körs

## Det skall ej vara stor bokstav på variablerna
## ändra så att det är punkt istället för kommateken
## . ,
## Skapa variablen bruttolön


månadslön = float(input("Skriv din månadslön?"))
kommunalskatt = månadslön * 0.2136
landstigsskatt = månadslön * 0.1148
nettolön = månadslön - kommunalskatt
årslön = 12 * månadslön



print("Månadslön{0:20}kr".format(round(månadslön)))
print("Kommunalskatt{0:20}kr".format(round(kommunalskatt)))
print("Landstigsskatt{0:20}kr".format(round(landstigsskatt)))
print("Nettolön{0:20}kr".format(round(nettolön)))

