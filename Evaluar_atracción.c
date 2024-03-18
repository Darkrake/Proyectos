#include <iostream>
using namespace std;

string evaluarAtraccion(int nivel) {
    switch(nivel) {
        case 1:
            return "Atracción fatal";
        case 2:
            return "Está tremenda/o";
        case 3:
            return "Para un rato y no más...";
        case 4:
            return "¡Que esperpento!";
        default:
            return "Valor de atracción no válido";
    }
}

int main() {
    int nivelAtraccion;
    cout << "Ingresa el nivel de atracción (1-4): ";
    cin >> nivelAtraccion;

    string resultado = evaluarAtraccion(nivelAtraccion);
    cout << "La evaluación de atracción es: " << resultado << endl;

    return 0;
}
