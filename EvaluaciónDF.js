function evaluarEntrenamiento(satisfaccion) {
    switch(satisfaccion) {
        case 1:
            return "Excelente entrenamiento";
        case 2:
            return "Buen entrenamiento";
        case 3:
            return "A medio gas";
        case 4:
            return "Energía por los suelos";
        case 5:
            return "Mejor me quedo en mi casa que no está mi crush";
        default:
            return "Valor de satisfacción no válido";
    }
}

// Ejemplo de uso
var satisfaccion = 5; // Cambia este valor para probar diferentes niveles de satisfacción
var resultado = evaluarEntrenamiento(satisfaccion);
console.log(resultado);
