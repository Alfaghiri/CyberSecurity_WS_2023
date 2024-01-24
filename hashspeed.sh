#!/bin/bash
#Dieses Bash-Skript führt Benchmark-Tests für verschiedene Hash-Modi in hashcat aus und s
#peichert die Ergebnisse in einer Datei. Es definiert eine Liste von Hashcat-Modi 
#(wie MD5, SHA1, etc.) und führt für jeden Modus einen Benchmark-Test aus. Die 
#Ergebnisse jedes Tests werden zusammen mit einer einführenden Beschreibung des 
#jeweiligen Modus in die Datei hashcat_benchmarks.txt geschrieben. Dieses Skript 
#ist nützlich, um die Leistung von hashcat auf dem aktuellen System für verschiedene 
#Hash-Typen zu messen und zu vergleichen.
# Define the output file
output_file="hashcat_benchmarks.txt"

# Define an array of Hashcat modes
declare -a modes=(0 100 1400 1700 1000 3200 8900 2500 200 3000)

# Loop through each mode and run the benchmark, appending the output to the file
for mode in "${modes[@]}"
do
    echo "Running benchmark for mode: $mode" | tee -a $output_file
    hashcat -b -m $mode | tee -a $output_file
done
        
