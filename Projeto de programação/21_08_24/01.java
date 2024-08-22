public static void main(String[] args) {
    public class Filme {
        String nome;
        int anoDeLancamento;
        boolean incluidoNoPlano;
        double somaDasAvaliacoes;
        int totalDeAvaliacoes;
        int duracaoEmMinutos;

        void exibirFichaTecnica() {
            System.out.println("Nome do filme: " + nome);
            System.out.println("Ano de lancamento: " + anoDeLancamento);
        }

        void avalia(double nota) {
            somaDasAvaliacoes += nota;
            totalDeAvaliacoes ++;
        }
        double pegaMedia(){
            return somaDasAvaliacoes/totalDeAvaliacoes;
        }
    }

    public class Principal {
        public static void main(String[] args) {
            Filme meuFilme = new Filme();
            meuFilme.nome = "O poderoso chefão";
            meuFilme.anoDeLancamento = 1970;
            meuFilme.duracaoEmMinutos = 180;

            meuFilme.exibirFichaTecnica();
            meuFilme.avalia(8);
            meuFilme.avalia(5);
            meuFilme.avalia(10);
        }
    }
}
