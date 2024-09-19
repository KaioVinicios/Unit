class ContaBancaria {
    protected double saldo;

    public void depositar(double valor) {
        saldo += valor;
    }

    public boolean sacar(double valor) {
        if (valor <= saldo) {
            saldo -= valor;
            return true;
        } else {
            System.out.println("Saldo insuficiente.");
            return false;
        }
    }

    public double consultarSaldo() {
        return saldo;
    }
}

class ContaCorrente extends ContaBancaria {
    private double tarifaMensal = 10.00; // Exemplo de tarifa mensal

    public void cobrarTarifaMensal() {
        if (saldo >= tarifaMensal) {
            saldo -= tarifaMensal;
        } else {
            System.out.println("Saldo insuficiente para cobrar a tarifa.");
        }
    }
}
