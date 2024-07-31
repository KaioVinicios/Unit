import java.util.ArrayList;
import java.util.Scanner;

public class Des03 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		ArrayList<Integer> lista = new ArrayList<>();
		
		for (int x = 0; x < 15; x++) {
            System.out.println("Digite um número: ");
            lista.add(input.nextInt());
		}
		 for (int i = lista.size() - 1; i >= 0; i--) {
	            System.out.println(lista.get(i));
	    }
        input.close();
	}
}