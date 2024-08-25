const vendasDiarias = [150, 200, 75, 300, 250, 400, 100];

function calcularMediaVendas(vendas) {
    let soma = vendas.reduce((total, venda) => total + venda, 0);
    return soma / vendas.length;
}

function encontrarMaiorEMenorVendas(vendas) {
    let maiorVenda = Math.max(...vendas);
    let menorVenda = Math.min(...vendas);
    let diaMaiorVenda = vendas.indexOf(maiorVenda);
    let diaMenorVenda = vendas.indexOf(menorVenda);
    return {
        maiorVenda,
        diaMaiorVenda,
        menorVenda,
        diaMenorVenda
    };
}

const diasDaSemana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado'];

const mediaVendas = calcularMediaVendas(vendasDiarias);
const { maiorVenda, diaMaiorVenda, menorVenda, diaMenorVenda } = encontrarMaiorEMenorVendas(vendasDiarias);

console.log('Análise de Vendas Semanais:');
console.log(`Média de vendas diárias: ${mediaVendas.toFixed(2)}`);
console.log(`Maior número de vendas: ${maiorVenda} (Dia: ${diasDaSemana[diaMaiorVenda]})`);
console.log(`Menor número de vendas: ${menorVenda} (Dia: ${diasDaSemana[diaMenorVenda]})`);