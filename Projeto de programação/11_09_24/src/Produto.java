public class Produto {
    private String nome = "violão";
    private double preco = 100.00;

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public double getPreco() {
        return preco;
    }
    public void setPreco(double preco) {
        this.preco = preco;
    }

    public void aplicarDesconto(double desconto) {
        this.preco -= this.preco*desconto;
    }

}
