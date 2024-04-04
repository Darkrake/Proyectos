#include <iostream>
#include <string>

using namespace std;

class ContratoAlquiler {
private:
    string propietario;
    string inquilino;
    double importeMensual;
    int duracionAnios;

public:
    // Constructor
    ContratoAlquiler(string prop, string inq, double importe, int duracion)
        : propietario(prop), inquilino(inq), importeMensual(importe), duracionAnios(duracion) {}

    // Método para imprimir el contrato
    void imprimirContrato() {
        cout << "Contrato de Alquiler" << endl;
        cout << "Propietario: " << propietario << endl;
        cout << "Inquilino: " << inquilino << endl;
        cout << "Importe mensual: $" << importeMensual << endl;
        cout << "Duración: " << duracionAnios << " años" << endl;
    }
};

int main() {
    // Crear un contrato de alquiler
    ContratoAlquiler contrato("Raquel Piqueras García", "Alexis Orosa Forte", 500, 1);

    // Imprimir el contrato
    contrato.imprimirContrato();

    return 0;
}
