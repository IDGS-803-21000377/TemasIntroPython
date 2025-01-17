from io import open
texto = ""

archivo=open("archivo.txt","r")


texto = archivo.read()

print(texto)

texto = archivo.readlines()

texto = archivo.read()
print(texto)

archivo.close()


