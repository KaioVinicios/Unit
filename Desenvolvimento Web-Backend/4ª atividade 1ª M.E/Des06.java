import java.util.Scanner;

public class Des06 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o primeiro valor: ");
        int valor1 = scanner.nextInt();

        int valor2;
        do {
            System.out.print("Digite o segundo valor (não pode ser zero): ");
            valor2 = scanner.nextInt();
        } while (valor2 == 0);

        System.out.println("Divisão dos valores inseridos: " + valor1/valor2);

        scanner.close();
    }
}
