import java.util.Scanner;

public class Des04 {
    public static int retornaSoma(int a, int b) {
        return a + b;
    }

    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        System.out.println(retornaSoma(2, 3));
        input.close();
    }
}
