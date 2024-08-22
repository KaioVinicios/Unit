// Desafio 17
let numeros = [2, 4, 6, 8]
let numeros_ao_quadrado = []
for(let c = 0; c < numeros.length; c++){
    numeros_ao_quadrado.push(numeros[c]**2)
}
console.log(numeros_ao_quadrado)

// Desafio 18 
let numeros0 = [5, 10, -3, 7]
result = true
for(let c = 0; c < numeros0.length; c++){
    if(numeros0[c] < 0){
        result = false
        break
    }
}
console.log(result)

// Desafio 19
let idades = [15, 22, 18, 30]
for(let c = 0; c < idades.length; c++){
    if(idades[c] >= 21){
        console.log(`O índice resultante é ${c}`)
        break
    }
}

// Desafio 20
let palavras = ['Eu', 'amo', 'JavaScript'];
let frase = '';
for (let c = 0; c < palavras.length; c++) {
    if (c > 0) {
        frase += ' ';
    }
    frase += palavras[i];
}
console.log(frase);