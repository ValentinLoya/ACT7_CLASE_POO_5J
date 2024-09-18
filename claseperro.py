print("Programacion POO")
# Definicion de clases
class Perro:
    def morder(self):
        print("El perro me mordio")
    def Datos_perro(self,nombre,edad):
        print(f"Nombre: {nombre} edad: {edad}")

#Zona de creacion de objeto
Pitbull=Perro()


#Zona de uso de objetos
Pitbull.Datos_perro("Jan",7)
Pitbull.morder()