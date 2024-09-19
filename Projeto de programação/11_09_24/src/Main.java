public class Main {
    public static void main(String[] args) {
        Produto produto = new Produto();
        produto.setPreco(70.00);
        produto.aplicarDesconto(0.1);
        System.out.println(produto.getPreco());
    }
}