package ME;

public class D05 {
    public static void main(String[] args) {
        int[] vetor = new int[3];
        int contador = 0;    
        int soma = 0;
        vetor[0] = 3;
        vetor[1] = 3;
        vetor[2] = 3;
        System.out.println(somaEmVetor(vetor, contador, soma));
    }
    
    public static int somaEmVetor(int vetor[], int contador, int soma) {
        if(contador < vetor.length){
            soma += vetor[contador];
            contador++; 
            return somaEmVetor(vetor, contador, soma);
        }
        else {
            return soma;
        }
    }
}
