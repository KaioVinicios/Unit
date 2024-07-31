let numero = parseInt(prompt("Digite um número para calcular o fatorial:"));
let fatorial = 1;

if (isNaN(numero)) {
  console.log("Por favor, insira um número válido.");
} else {
  let i = 1;
  do {
    fatorial *= i;
    i++;
  } while (i <= numero);

  console.log(`O fatorial de ${numero} é ${fatorial}`);
}
