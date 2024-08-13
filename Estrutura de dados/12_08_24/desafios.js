// 6
let primeiro = new Array()
let segundo = new Array('verde', 'azul', 'vermelho')

console.log(segundo)

// 7
let animais = ['cachorro', 'gato', 'pássaro']
console.log(animais[1])

// 8
let numeros = new Array(1,2,3)
numeros.push(4)
console.log(numeros)

// 9
let letras = new Array('a', 'b', 'c', 'd')
letras.pop()
console.log(letras)

// 10
let cidades = new Array('São Paulo', 'Rio de Janeiro')
cidades.unshift('Belo Horizonte')
console.log(cidades)

// 11
let dias = new Array('segunda', 'terça', 'quarta')
dias.shift()
console.log(dias)

// 12 
let alimentos = new Array('maçã', 'banana', 'laranja')
console.log(alimentos.indexOf('banana'))

// 13 
let animais0 = new Array('leão', 'tigre', 'urso')
console.log(animais0.includes('tigre'))

// 14
let numeros0 = new Array(5,10,15)
for(let i = 0; i < numeros0.length; i++) console.log(numeros0[i])

// 15
let numeros1 = new Array(10, 20, 30, 40, 50)
let result = 0
for(let i = 0; i < numeros1.length; i++) result += numeros1[i]

// 16
let numeros2 = new Array(45, 78, 12, 89, 34)
let maior = 0
for(let i = 0; i < numeros2.length; i++) {
    if(numeros2[i] > maior){
        maior = numeros2[i]
    }
}
console.log(maior)
