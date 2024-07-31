import java.util.Scanner;

public class Des04 {
    public static void main(String args[]) {
        Scanner myObj = new Scanner(System.in);
    
        System.out.println("Digite o primeiro número: ");
        int primeiro = myObj.nextInt();   
        
        myObj.nextLine();
        
        System.out.println("Digite o operador: ");
        String operador = myObj.nextLine();   
        
        System.out.println("Digite o segundo número: ");
        int segundo = myObj.nextInt();   
        int result = 0;

        switch(operador){
            case "+":
                result = primeiro + segundo;
                break;
            case "-":
                result = primeiro - segundo;
                break;
            case "/":
                result = primeiro / segundo;
                break;
            case "*":
                result = primeiro * segundo;
                break;
            default:
                System.out.println("Operador inválido");
        }         

        System.out.println("Resultado: " + result);
        myObj.close();
    }
}
