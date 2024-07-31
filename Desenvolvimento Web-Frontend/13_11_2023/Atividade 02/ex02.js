const valores = [3, 5, 7, 9, 11];
valores.forEach((valor, index, array) => {
  array[index] = valor * 2;
});

console.log("Array modificado: " + valores);
