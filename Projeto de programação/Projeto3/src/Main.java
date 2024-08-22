public class Main {
    public static void main(String[] args) {
        Autor autor1 = new Autor("George Orwell");
        Autor autor2 = new Autor("J.K. Rowling");

        Livro livro1 = new Livro("1984", 1949, autor1);
        Livro livro2 = new Livro("Harry Potter e a Pedra Filosofal", 1997, autor2);

        Biblioteca biblioteca = new Biblioteca();
        biblioteca.adicionarAutor(autor1);
        biblioteca.adicionarAutor(autor2);
        biblioteca.adicionarLivro(livro1);
        biblioteca.adicionarLivro(livro2);

        biblioteca.exibirInformacoes();
    }
}
