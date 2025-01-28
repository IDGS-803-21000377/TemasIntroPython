import os
from io import open


class Diccion:

    entr = 0 
    salida = 0
    def __init__(self,a,b):
        self.entr = a
        self.salida = b

    def addWord(self):
        
        print("dame la palabra en español:")
        self.entr = input("palabra en español: ")
        print("dame la palabra en ingles:")
        self.salida = input("palabra en ingles: ")
        archivo = open("diccionario.txt", "a")
    
        archivo.write(self.entr)    
        archivo.write(" ")      
        archivo.write(self.salida)
        archivo.write("\n")     
        archivo.close()
        print("la palabra {} se ha añadido al diccionario".format(self.entr))           
        input("presiona enter para continuar")



    def findWord(self):

        txt = ""
        print("Elige el idioma entre el español o el ingles")
        print("1-español")
        print("2-ingles")

        opcion = int(input("elige una opcion: "))


        if opcion == 1:
            print("dame la palabra en español:")
            self.entr = input("palabra en español: ")
        if opcion == 2:

            print("dame la palabra en ingles:")
            self.salida = input("palabra en ingles:")

        archivo = open("diccionario.txt","r")

        for linea in archivo :
            txt += linea
        archivo.close()



        if self.entr in txt:
            print("la palabra {} se ha encontrado en el diccionario".format(self.entr))
        else:
            print("la palabra {} no se ha encontrado en el diccionario".format(self.entr))
        if self.salida in txt:
            print("la palabra {} se ha encontrado en el diccionario".format(self.salida))
        else:
            print("la palabra {} no se ha encontrado en el diccionario".format(self.salida))
        input("presiona enter para continuar")

            

                        

                        

def main():  
    obj = Diccion("","")

    while True:
        os.system('cls')
        print("menu de opciones:")
        print("1-añadir palabra")
        print("2-buscar palabra")
        print("3-salir")

        opcion = int(input("elige una opcion: "))
        if opcion == 1:
            obj.addWord()
        if opcion == 2:
            obj.findWord()
        if opcion == 3:

            break





if __name__ == "__main__":
    main()