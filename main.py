# OpenBootcamp Curso Python Ejercicio 6

# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# - Color
# - Ruedas
# - Puertas
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# - Velocidad
# - Cilindrada
# Por último, crearéis un objeto de la clase Coche y lo mostraréis por consola.

class Vehiculo:
    color = "Rojo"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 120
    cilindrada = 1200

coche = Coche()
print("Color del coche: ", coche.color)
print("Cilindrada del coche: ", coche.cilindrada)
print("Ruedas del coche: ", coche.ruedas)
print("Velocidad del coche: ", coche.velocidad)
print("Puertas del coche: ", coche.puertas)
