function menor(a, b, c) {
    if ((a < b) && (a < c)) {
        return a 
    }
    else if ((b < a) && (b < c)) {
        return b 
    }
    else {
        return c
    }
}
const resultado = menor(2,6,8)
console.log(resultado)