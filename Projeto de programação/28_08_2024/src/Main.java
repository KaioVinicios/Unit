public class Main {
    public static void main(String[] args) {
        Aluno aluno1 = new Aluno("João", 20);
        Aluno aluno3 = new Aluno("Pedro", 19);
        Aluno aluno2 = new Aluno("Maria", 22);
        aluno1.exibirDetalhes();
        aluno2.exibirDetalhes();
        aluno3.exibirDetalhes();

        Fruta fruta1 = new Fruta("Maçã", "Vermelha");
        Fruta fruta2 = new Fruta("Banana", "Amarela");
        Fruta fruta3 = new Fruta("Uva", "Roxa");


        Inventario inventario = new Inventario();
        inventario.adicionarFruta(fruta1);
        inventario.adicionarFruta(fruta2);
        inventario.adicionarFruta(fruta3);

        inventario.exibirFrutas();
    }
}