import java.util.Scanner;

public class ex02 {
    public static void main(String args[]) {
      int num1 = 0, num2 = 0;
      
      Scanner input = new Scanner(System.in);
        System.out.println("Digite o 1º: ");
        num1 = input.nextInt();
        System.out.println("Digite o 2º: ");
        num2 = input.nextInt();

        int divisao_inteiro = (int) num1/num2;
        double divisao_total = (double) num1/num2;
    
        System.out.println("Divisão inteira exata: " + divisao_inteiro + " Divisão total: " + divisao_total);
        input.close();
    }
}
