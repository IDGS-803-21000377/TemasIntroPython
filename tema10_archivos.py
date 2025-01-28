from io import open

texto = "una linea\n"
archivo = open("archivo.txt", "a")
archivo.write(texto)

texto = "una linea nueva\n"
archivo.write(texto)

texto = "una linea nueva tres\n"
archivo.write(texto)

archivo.close()
