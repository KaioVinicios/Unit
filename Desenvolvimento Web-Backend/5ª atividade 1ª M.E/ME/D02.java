package ME;
import java.util.Scanner;

public class D02 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Digite o número para calcular a raiz quadrada: ");
        double num =  input.nextDouble();
        System.out.println("A raiz quadrada de " + num + " é: " + Math.sqrt(num));
        input.close();
    }
}
