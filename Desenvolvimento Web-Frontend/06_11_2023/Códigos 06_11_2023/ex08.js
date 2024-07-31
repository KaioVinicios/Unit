const contElem = () => {
    let contador = 0
    let array = {};
    while (contador <= 10) {
        array.push(contador)
        contador++ 
    }
    return array.length;
};

console.log(contElem())