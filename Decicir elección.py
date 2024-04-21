import random

def decidir_eleccion():
    opciones = [
        "Ver una película juntos",
        "Salir a cenar",
        "Hacer un picnic en el parque",
        "Visitar un museo",
        "Cocinar juntos en casa",
        "Ir a un concierto",
        "Dar un paseo por la playa",
        "Jugar juegos de mesa",
        "Ir a un parque de diversiones",
        "Hacer deporte juntos"
    ]
    
    # Elegir una opción al azar
    eleccion = random.choice(opciones)
    
    return eleccion

# Función principal
def main():
    print("¡Bienvenido a la decisión de actividades en pareja!")
    print("Te sugerimos la siguiente actividad para disfrutar juntos:")
    print(decidir_eleccion())

if __name__ == "__main__":
    main()
