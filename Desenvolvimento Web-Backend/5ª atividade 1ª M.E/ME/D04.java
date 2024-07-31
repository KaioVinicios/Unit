package ME;
import java.util.Scanner;

public class D04 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Digite o primeiro, segundo e terceiro número, respectivamente: ");
        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();
        System.out.println(retornaMenor(a, b, c));
        input.close();
    }
    public static int retornaMenor(int a, int b, int c) {
        if(a < b && a < c){
            return a; 
        }
        else if (b < a && b < c) {
            return b;
        }
        else {
            return c;
        }
    }
}