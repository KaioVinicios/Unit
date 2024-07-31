import java.util.Scanner;

public class Des02 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int matriz[][] = new int[3][3];
        for(int x = 0; x < matriz.length; x++){
            for (int y = 0; x < matriz[x].length; y++){
                matriz[x][y] = input.nextInt();
                System.out.println(matriz[x][y]);
            }
        }
        input.close();
    }
}