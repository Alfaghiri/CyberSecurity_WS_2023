#Dieses Python-Skript generiert eine umfangreiche Liste möglicher Passwörter basierend auf persönlichen 
#Informationen (Vorname, Nachname, Geburtsdatum) und einer vorgegebenen Wortliste. Es liest Daten aus 
#einer JSON-Datei, erstellt für jede Person eine Hash-Datei (*_hash.txt) und eine zugehörige 
#Passwortliste (*_list.txt). Die generierte Passwortliste kombiniert persönliche Informationen mit 
#verschiedenen Symbolen und Wörtern aus der vorgegebenen Liste in mehreren Mustern, um eine breite Palette 
#potenzieller Passwörter zu erstellen.
import json
def generiere_passwort_liste(vorname, nachname, geburtsdatum):
    passwort_liste = []

    # Zerlege das Geburtsdatum in Tag, Monat und Jahr
    tag, monat, jahr = geburtsdatum.split(".")

    # Erstelle Listen für die verschiedenen Kombinationen
    namen = [vorname, nachname]
    daten = [jahr, monat, tag]
    symbole = ["@", "#","$","%","?","!","&","/",]
    wordlist =['admin','flower','1q2w3e4r','casper','turtle','asdf','qweasd','super','water','root','qwerty','dragon','computer','love','forever','Pass','Passowrd','Admin','Plus','Salzburg','Wien','Tirol','Graz','2024','2023','Au','Austria']

    # Kombiniere Namen mit Datenteilen und füge Symbole hinzu
    for name in namen:
        for datum in daten:
            for symbol in symbole:
                for word in wordlist:
                    passwort_liste.append(name)
                    passwort_liste.append(word +name + symbol + datum)
                    passwort_liste.append(datum + symbol + name)
                    passwort_liste.append(name+datum)
                    passwort_liste.append(datum+name)
                    passwort_liste.append(name+symbol+symbol+datum)
                    passwort_liste.append(word+datum+symbol + symbol + datum)
                    passwort_liste.append(datum + name + symbol + datum)
                    passwort_liste.append(datum + word +symbol + name)
                    passwort_liste.append(name + datum + symbol + word)
                    passwort_liste.append(symbol + name + datum + symbol)
                    passwort_liste.append(name + datum + name + symbol)
                    passwort_liste.append(symbol + name + word + datum + symbol + datum + name)
                    passwort_liste.append(datum + symbol + word +datum + name + symbol)
                    passwort_liste.append(name + datum + symbol + datum + name + symbol)
                    passwort_liste.append(datum + name + symbol  + datum + symbol + name)
                    passwort_liste.append(name + datum + symbol + word + datum + name + symbol)
                    passwort_liste.append(name + datum + symbol)
                    passwort_liste.append(symbol + name + datum)
                    passwort_liste.append(datum + name + symbol)
                    passwort_liste.append(name + symbol + datum)
                    passwort_liste.append(symbol + datum + name)

    return passwort_liste
with open ('data.json') as f:
    dates = json.load(f)
for data in dates:
    with open(f'{data[0]}_hash.txt', "w") as f:
        f.write(data[2])
    vorname = data[3]
    nachname = data[4]
    geburtsdatum = data[5]  
    passwoerter = generiere_passwort_liste(vorname, nachname, geburtsdatum)
    with open(f'{data[0]}_list.txt', "w") as file:
        for passwort in passwoerter:
            file.write(passwort + "\n")


