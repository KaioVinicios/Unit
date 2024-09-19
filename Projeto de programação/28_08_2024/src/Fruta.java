public class Fruta {
    private String nome;
    private String cor;

    public Fruta(String nome, String cor) {
        this.nome = nome;
        this.cor = cor;
    }

    public String getNome() {
        return nome;
    }

    public String getCor() {
        return cor;
    }

    public void exibirDetalhes() {
        System.out.println("Fruta: " + nome + ", Cor: " + cor);
    }
}
