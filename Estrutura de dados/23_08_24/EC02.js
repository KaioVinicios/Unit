const estoque = [
    { produto: 'Camiseta', quantidade: 10 },
    { produto: 'Calça', quantidade: 15 },
    { produto: 'Tênis', quantidade: 4 },
    { produto: 'Boné', quantidade: 6 }
];

function adicionarEstoque(produtoNome, quantidade) {
    const produto = estoque.find(item => item.produto === produtoNome);
    if (produto) {
        produto.quantidade += quantidade;
    } else {
        console.log(`Produto ${produtoNome} não encontrado.`);
    }
}

function removerEstoque(produtoNome, quantidade) {
    const produto = estoque.find(item => item.produto === produtoNome);
    if (produto) {
        if (produto.quantidade >= quantidade) {
            produto.quantidade -= quantidade;
        } else {
            console.log(`Quantidade insuficiente de ${produtoNome} em estoque.`);
        }
    } else {
        console.log(`Produto ${produtoNome} não encontrado.`);
    }
}

function verificarEstoqueBaixo() {
    estoque.forEach(item => {
        if (item.quantidade < 5) {
            console.log(`Alerta: Estoque baixo de ${item.produto} (${item.quantidade} unidades).`);
        }
    });
}

function exibirEstoque() {
    console.log('Estoque atualizado:');
    estoque.forEach(item => {
        console.log(`${item.produto}: ${item.quantidade} unidades`);
    });
    console.log('------------------------------------');
}
