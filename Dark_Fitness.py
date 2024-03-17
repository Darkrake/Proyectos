class Socio:
    def __init__(self, nombre, edad, email, telefono):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.telefono = telefono

class GimnasioDarkFitness:
    def __init__(self):
        self.socios = []

    def registrar_socio(self, socio):
        self.socios.append(socio)
        print(f"Socio {socio.nombre} registrado exitosamente en Dark Fitness.")

    def mostrar_socios(self):
        print("Lista de Socios de Dark Fitness:")
        for i, socio in enumerate(self.socios, 1):
            print(f"{i}. Nombre: {socio.nombre}, Edad: {socio.edad}, Email: {socio.email}, Teléfono: {socio.telefono}")

# Función para registrar un nuevo socio
def registrar_nuevo_socio(gimnasio):
    nombre = input("Ingrese el nombre del socio: ")
    edad = int(input("Ingrese la edad del socio: "))
    email = input("Ingrese el email del socio: ")
    telefono = input("Ingrese el número de teléfono del socio: ")
    socio_nuevo = Socio(nombre, edad, email, telefono)
    gimnasio.registrar_socio(socio_nuevo)

# Función principal
def main():
    gimnasio = GimnasioDarkFitness()
    while True:
        print("\nBienvenido a Dark Fitness")
        print("1. Registrar nuevo socio")
        print("2. Mostrar lista de socios")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_nuevo_socio(gimnasio)
        elif opcion == "2":
            gimnasio.mostrar_socios()
        elif opcion == "3":
            print("Gracias por usar Dark Fitness. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
