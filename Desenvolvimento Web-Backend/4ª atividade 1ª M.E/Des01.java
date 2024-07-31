import java.util.Scanner;

public class Des01 {
    public static void main(String args[]) {
        Scanner myObj = new Scanner(System.in);
    
        System.out.println("Digite a distancia percorrida em KM");
        float distanciaPercorrida = myObj.nextFloat();   
        System.out.println("Digite o tempo decorrido em horas");
        float tempoDecorrido = myObj.nextFloat();
        float velocidadeMedia = distanciaPercorrida/tempoDecorrido;
        if(velocidadeMedia >= 120.00){
            System.out.println("Voce foi multado.");
        };
        System.out.println("A velocidade media e de " + velocidadeMedia);
        myObj.close();
    }
}