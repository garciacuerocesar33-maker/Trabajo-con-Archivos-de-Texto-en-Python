# Escritura en el archivo my_notes.txt
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Nota 1: Mañana me ire de viaje y tengo que dejar limpia la casa.\n")
    file.write("Nota 2: Tengo que dejar preparada la maleta para el viaje de mañana.\n")
    file.write("Nota 3: Tengo que salir alas 9:30 para llegar temprano para viajar.\n")

# Lectura del archivo my_notes.txt línea por línea
with open("my_notes.txt", "r") as file:
    # Leer línea por línea usando readline()
    line = file.readline()
    while line:
        print(line.strip())  # Imprime la línea sin el salto de línea final
        line = file.readline()
