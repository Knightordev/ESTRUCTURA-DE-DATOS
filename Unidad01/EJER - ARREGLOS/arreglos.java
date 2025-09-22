import java.util.Scanner;

public class arreglos {

    private static double[][] ventas = new double[12][3];
    private static String[] meses = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                                    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};
    private static String[] departamentos = {"Ropa", "Deportes", "Juguetería"};

    public static void insertarVenta(int mes, int depto, double monto) {
        ventas[mes][depto] = monto;
        System.out.println("Venta registrada: " + meses[mes] + " - " + departamentos[depto] + " = $" + monto);
    }


    public static void buscarVenta(int mes, int depto) {
        double monto = ventas[mes][depto];
        if (monto != 0) {
            System.out.println("Venta encontrada: " + meses[mes] + " - " + departamentos[depto] + " = $" + monto);
        } else {
            System.out.println("No hay venta registrada en " + meses[mes] + " para " + departamentos[depto]);
        }
    }


    public static void eliminarVenta(int mes, int depto) {
        ventas[mes][depto] = 0;
        System.out.println("Venta eliminada en " + meses[mes] + " - " + departamentos[depto]);
    }

    public static void mostrarVentas() {
        System.out.println("\n--- Ventas Registradas ---");
        System.out.print("Mes\\Depto\t");
        for (String dep : departamentos) {
            System.out.print(dep + "\t");
        }
        System.out.println();
        for (int i = 0; i < 12; i++) {
            System.out.print(meses[i] + "\t");
            for (int j = 0; j < 3; j++) {
                System.out.print(ventas[i][j] + "\t\t");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n--- MENÚ ---");
            System.out.println("1. Insertar venta");
            System.out.println("2. Buscar venta");
            System.out.println("3. Eliminar venta");
            System.out.println("4. Mostrar todas las ventas");
            System.out.println("5. Salir");
            System.out.print("Elige una opción: ");
            opcion = sc.nextInt();

            switch (opcion) {
                case 1:
                    System.out.print("Mes (0-11): ");
                    int mesIns = sc.nextInt();
                    System.out.print("Departamento (0=Ropa, 1=Deportes, 2=Juguetería): ");
                    int depIns = sc.nextInt();
                    System.out.print("Monto: ");
                    double monto = sc.nextDouble();
                    insertarVenta(mesIns, depIns, monto);
                    break;
                case 2:
                    System.out.print("Mes (0-11): ");
                    int mesBus = sc.nextInt();
                    System.out.print("Departamento (0=Ropa, 1=Deportes, 2=Juguetería): ");
                    int depBus = sc.nextInt();
                    buscarVenta(mesBus, depBus);
                    break;
                case 3:
                    System.out.print("Mes (0-11): ");
                    int mesDel = sc.nextInt();
                    System.out.print("Departamento (0=Ropa, 1=Deportes, 2=Juguetería): ");
                    int depDel = sc.nextInt();
                    eliminarVenta(mesDel, depDel);
                    break;
                case 4:
                    mostrarVentas();
                    break;
                case 5:
                    System.out.println("Saliendo...");
                    break;
                default:
                    System.out.println("Opción inválida");
            }
        } while (opcion != 5);

        sc.close();
    }
}
