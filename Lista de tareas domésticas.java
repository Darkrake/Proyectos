public class ListaTareasDomesticas {
    public static void main(String[] args) {
        // Crear un arreglo para almacenar las tareas domésticas
        String[] tareas = {
            "Hacer la colada",
            "Planchar",
            "Pasar la mopa",
            "Fregar los trastos",
            "Quitar el polvo"
        };

        // Imprimir la lista de tareas
        System.out.println("Tareas domésticas:");
        for (String tarea : tareas) {
            System.out.println("- " + tarea);
        }
    }
}
