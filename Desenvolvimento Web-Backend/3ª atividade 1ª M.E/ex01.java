import java.util.Scanner;

public class ex01 {
    public static void main(String args[]) {
      float num1 = 0, num2 = 0, num3 = 0;
      
      Scanner input = new Scanner(System.in);
        System.out.println("Digite o 1º: ");
        num1 = input.nextFloat();
        System.out.println("Digite o 2º: ");
        num2 = input.nextFloat();
        System.out.println("Digite o 3º: ");
        num3 = input.nextFloat();
        float media = (num1 + num2 + num3)/3;
    
        System.out.println("Média = " + media);
        input.close();
    }
}
