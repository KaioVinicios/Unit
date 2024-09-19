class Carro {
    private String nomeModelo;
    private double[] precos = new double[3];

    public void setNomeModelo(String nomeModelo) {
        this.nomeModelo = nomeModelo;
    }

    public void setPrecoAno(int anoIndex, double preco) {
        if (anoIndex >= 0 && anoIndex < 3) {
            precos[anoIndex] = preco;
        } else {
            System.out.println("Índice de ano inválido.");
        }
    }

    public double calcularMenorPreco() {
        double menorPreco = precos[0];
        for (double preco : precos) {
            if (preco < menorPreco) {
                menorPreco = preco;
            }
        }
        return menorPreco;
    }

    public double calcularMaiorPreco() {
        double maiorPreco = precos[0];
        for (double preco : precos) {
            if (preco > maiorPreco) {
                maiorPreco = preco;
            }
        }
        return maiorPreco;
    }

    public void exibirInformacoes() {
        System.out.println("Modelo: " + nomeModelo);
        System.out.println("Preços ao longo de 3 anos:");
        for (int i = 0; i < precos.length; i++) {
            System.out.println("Ano " + (i + 1) + ": R$ " + precos[i]);
        }
        System.out.println("Menor preço: R$ " + calcularMenorPreco());
        System.out.println("Maior preço: R$ " + calcularMaiorPreco());
    }
}

class ModeloCarro extends Carro {
    public ModeloCarro(String nomeModelo, double precoAno1, double precoAno2, double precoAno3) {
        setNomeModelo(nomeModelo);
        setPrecoAno(0, precoAno1);
        setPrecoAno(1, precoAno2);
        setPrecoAno(2, precoAno3);
    }
}