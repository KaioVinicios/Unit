const alunos = [
    { nome: 'Alice', notas: [8, 6, 7, 9, 5] },
    { nome: 'Bruno', notas: [10, 8, 9, 7, 6] },
    { nome: 'Carla', notas: [7, 5, 6, 8, 4] }
];

function calcularMedia(notas) {
    let soma = notas.reduce((total, nota) => total + nota, 0);
    return soma / notas.length;
}

function precisaRecuperacao(notas) {
    return notas.some(nota => nota < 7);
}

function notaMaisAlta(notas) {
    return Math.max(...notas);
}

function notaMaisBaixa(notas) {
    return Math.min(...notas);
}

alunos.forEach(aluno => {
    const media = calcularMedia(aluno.notas);
    const emRecuperacao = precisaRecuperacao(aluno.notas);
    const maiorNota = notaMaisAlta(aluno.notas);
    const menorNota = notaMaisBaixa(aluno.notas);

    console.log(`Aluno: ${aluno.nome}`);
    console.log(`Média: ${media.toFixed(2)}`);
    console.log(`Precisa de recuperação: ${emRecuperacao ? 'Sim' : 'Não'}`);
    console.log(`Nota mais alta: ${maiorNota}`);
    console.log(`Nota mais baixa: ${menorNota}`);
    console.log('------------------------------------');
});