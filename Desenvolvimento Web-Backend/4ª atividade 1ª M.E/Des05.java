import java.util.Scanner;

public class Des05 {
    public static void main(String args[]) {
        Scanner myObj = new Scanner(System.in);
        
        for(int i = 0; i < 50; i++){
            System.out.println(i+1 + "ª " + i + " x " + 7 + " = " + i*7);
        }

        //System.out.println("Resultado: " + result);
        myObj.close();
    }
}

