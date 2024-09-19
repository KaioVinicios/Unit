import java.util.ArrayList;
import java.util.List;

public class Inventario {
    private List<Fruta> frutas;

    public Inventario() {
        this.frutas = new ArrayList<>();
    }

    public void adicionarFruta(Fruta fruta) {
        frutas.add(fruta);
    }

    public void exibirFrutas() {
        for (Fruta fruta : frutas) {
            fruta.exibirDetalhes();
        }
    }
}
