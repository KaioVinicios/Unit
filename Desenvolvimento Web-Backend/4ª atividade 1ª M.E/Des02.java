import java.util.Scanner;

public class Des02 {
    public static void main(String args[]) {
        Scanner myObj = new Scanner(System.in);
    
        System.out.println("Digite sua idade: ");
        int idade = myObj.nextInt();   
        if(idade > 16 && 69 > idade){
            System.out.println("Voce esta apto para doar.");
        }
        else {
            System.out.println("Voce nao esta apto para doar.");
        }
        System.out.println("Voce nasceu em " + (2024-idade));
        myObj.close();
    }
}