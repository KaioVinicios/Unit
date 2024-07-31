package ME;
import java.util.Scanner;

public class D03 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int matriz[][] = new int[3][3];
        for(int linha = 0; linha < matriz.length; linha++) {
            for(int coluna = 0; coluna < matriz[linha].length; coluna++){
                System.out.println("Digite um elemento: ");
                matriz[linha][coluna] = input.nextInt();
            }
        }
        for(int linha = 0; linha < matriz.length; linha++) {
            for(int coluna = 0; coluna < matriz[linha].length; coluna++){
                int elementoMultiplicado = matriz[linha][coluna] * 5; 
                System.out.println(elementoMultiplicado);
            }
        }
        input.close();
    }
}
