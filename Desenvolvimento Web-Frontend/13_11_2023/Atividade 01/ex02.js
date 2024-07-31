let soma = 0;

do {
    let numero = parseFloat(prompt("Digite um número:"));
    if (!isNaN(numero)) {
        soma += numero;
    } else { alert("Por favor, insira um número válido."); }

} while (soma < 100);

console.log("A soma dos números atingiu ou ultrapassou 100.");
