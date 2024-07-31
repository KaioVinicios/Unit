import java.util.Scanner;

public class ex03 {
    public static void main(String[] axsrgs) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Número de carros vendidos: ");
        int numCarrosVendidos = scanner.nextInt();

        System.out.print("Valor total das vendas: ");
        double valorTotalVendas = scanner.nextDouble();

        System.out.print("Salário fixo: ");
        double salarioFixo = scanner.nextDouble();

        System.out.print("Valor por carro vendido: ");
        double valorPorCarroVendido = scanner.nextDouble();

        double comissao = 0.05 * valorTotalVendas;

        double salarioFinal = salarioFixo + comissao + (valorPorCarroVendido * numCarrosVendidos);

        System.out.println("Salário final do vendedor: R$" + salarioFinal);
        scanner.close();
    }
}
