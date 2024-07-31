let soma = 0;
let i = 0;

while (i < 20) {
  let valor = prompt("Digite um valor real: ");
  valor = parseFloat(valor);
  soma += valor;
  i++;
}

console.log("A soma dos valores é: " + soma);
