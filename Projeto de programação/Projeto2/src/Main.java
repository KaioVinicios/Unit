public class Main {
    public static void main(String[] args) {
        Pessoa pessoa = new Pessoa();
        pessoa.dizerOla();

        Calculadora calculadora = new Calculadora();
        System.out.println("Dobro de 5: " + calculadora.dobrar(5));

        Musica musica = new Musica("Bohemian Rhapsody", "Queen", 1975);
        musica.exibirFichaTecnica();
        musica.avaliar(5);
        musica.avaliar(4);
        musica.exibirFichaTecnica();

        Carro carro = new Carro("Fusca", 1970, "Azul");
        carro.exibirFichaTecnica();
        System.out.println("Idade do carro: " + carro.calcularIdade() + " anos");

        Aluno aluno = new Aluno("João", 20);
        aluno.exibirInformacoes();
    }
}