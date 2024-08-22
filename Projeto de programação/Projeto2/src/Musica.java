public class Musica {
    String titulo;
    String artista;
    int anoLancamento;
    int avaliacao;
    int numAvaliacoes;

    public Musica(String titulo, String artista, int anoLancamento) {
        this.titulo = titulo;
        this.artista = artista;
        this.anoLancamento = anoLancamento;
        this.avaliacao = 0;
        this.numAvaliacoes = 0;
    }

    public void exibirFichaTecnica() {
        System.out.println("Título: " + titulo);
        System.out.println("Artista: " + artista);
        System.out.println("Ano de Lançamento: " + anoLancamento);
        System.out.println("Avaliação: " + (numAvaliacoes > 0 ? (double)avaliacao / numAvaliacoes : "Nenhuma Avaliação"));
    }

    public void avaliar(int nota) {
        this.avaliacao += nota;
        this.numAvaliacoes++;
    }
}
