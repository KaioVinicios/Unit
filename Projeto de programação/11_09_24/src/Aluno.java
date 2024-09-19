import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Aluno {
    private String nome;
    private List<Double> notas  = new ArrayList<>(Arrays.asList(6.0, 7.0, 5.0));

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public List<Double> getNotas() {
        return notas;
    }
    public void setNotas(List<Double> notas) {
        this.notas = notas;
    }

    public double mediaNotas() {
        double media = 0;
        for (Double nota : notas) {
            media += nota;
        }
        return media / notas.size();
    }
}

