import java.util.Scanner;

public class Des07 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 1
        System.out.print("Digite um número: ");
        int numero = scanner.nextInt();
        if (numero > 0) {
            System.out.println("O número é positivo.");
        } else if (numero < 0) {
            System.out.println("O número é negativo.");
        } else {
            System.out.println("O número é zero.");
        }

        // 2 
        System.out.println("\nTabuada do 1 a 10:");
        for (int i = 1; i <= 10; i++) {
            for (int j = 1; j <= 10; j++) {
                System.out.println(i + " x " + j + " = " + (i * j));
            }
        }

        // 3
        int[] valores = new int[3];
        for (int i = 0; i < 3; i++) {
            System.out.print("\nDigite o " + (i + 1) + "º valor: ");
            valores[i] = scanner.nextInt();
            for (int j = 0; j < i; j++) {
                if (valores[i] == valores[j]) {
                    System.out.println("Valor já digitado. Por favor, digite um valor diferente.");
                    i--;
                    break;
                }
            }
        }
        for (int i = 0; i < valores.length - 1; i++) {
            for (int j = i + 1; j < valores.length; j++) {
                if (valores[i] < valores[j]) {
                    int temp = valores[i];
                    valores[i] = valores[j];
                    valores[j] = temp;
                }
            }
        }
        System.out.println("\nValores em ordem decrescente:");
        for (int valor : valores) {
            System.out.println(valor);
        }

        scanner.close();
    }
}
