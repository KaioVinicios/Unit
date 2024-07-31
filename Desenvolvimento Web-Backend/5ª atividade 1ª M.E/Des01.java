import java.util.Scanner;

public class Des01 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        double notas[] = new double[10];
        double soma = 0;
        for (int i = 0; i < notas.length; i++) {
            System.out.println("Digite a nota do " + (i+1) + "º aluno:");
            notas[i] = input.nextDouble();
            soma += notas[i];
        }
        System.out.println(notas);
        double media = soma/notas.length;
        for (int x = 0; x < notas.length; x++){
            if(notas[x] > media){
                System.out.println("O aluno " + (x+1) + "º teve nota acima da média");
            }
        }
        input.close();
    }
}