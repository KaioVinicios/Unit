import java.util.ArrayList;
import java.util.List;

class Biblioteca {
    private List<Autor> autores;
    private List<Livro> livros;

    public Biblioteca() {
        autores = new ArrayList<>();
        livros = new ArrayList<>();
    }

    public void adicionarAutor(Autor autor) {
        autores.add(autor);
    }

    public void adicionarLivro(Livro livro) {
        livros.add(livro);
    }

    public void exibirInformacoes() {
        System.out.println("Informações da Biblioteca:");
        for (Autor autor : autores) {
            autor.exibirInformacoes();
        }
        for (Livro livro : livros) {
            livro.exibirInformacoes();
        }
    }
}
