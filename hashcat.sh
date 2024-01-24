#!/bin/bash
#Dieses Bash-Skript verwendet hashcat zur Passwortwiederherstellung, indem es Hashes 
#aus *_hash.txt-Dateien mit Wortlisten aus *_list.txt-Dateien abgleicht. Es verarbeitet 
#Paare dieser Dateien für Nummern von 1 bis max_nummer (standardmäßig 30) und speichert 
#die Ergebnisse in gefundene_passwoerter.txt. Das Format der Ausgabe ist entweder Nummer: gefundenes 
#Passwort oder Nummer: Nicht gefunden, je nachdem, ob ein Passwort erfolgreich wiederhergestellt wurde
#oder nicht.
output_file="gefundene_passwoerter.txt"
> "$output_file"

max_nummer=30

# Schleife durch die Nummern
for i in $(seq 1 $max_nummer); do
    list_file="${i}_list.txt"
    hash_file="${i}_hash.txt"

    if [[ -f "$list_file" && -f "$hash_file" ]]; then
        gefundene_passwoerter=$(hashcat -m 3200 "$hash_file" "$list_file")
        if [ -n "$gefundene_passwoerter" ]; then
            echo "$i: $gefundene_passwoerter" >> "$output_file"
        else
            # Meldung für nicht gefundene Passwörter
            echo "$i: Nicht gefunden" >> "$output_file"
        fi
    else
        echo "List- oder Hash-Datei für Nummer $i nicht gefunden" >> "$output_file"
    fi
done

echo "Vorgang abgeschlossen. Ergebnisse in $output_file."
