function fatorial(n) {
    var total = 0;
    for(var i =1; i < n; i++) {
        if (i===1) {
            total = n * (n - 1);
        }
        else {
            total = total * (n - i);
        }
    }
    return total;
}

console.log(fatorial(5))