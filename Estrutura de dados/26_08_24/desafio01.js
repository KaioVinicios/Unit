// Esqueleto - Pilha
// vamos usar classe ( vamos trabalhar com objetos)
function Stack() {
    var items = []
    
    this.print = function() {
        //imprime a pilha no console
        console.log(items)
    }

    this.push = function(element) { 
        //adiciona um novo item a pilha
        items.push(element)
        this.print()
    }   

    this.pop = function() {
        items.pop()
        this.print()
    }
}

let teste = new Stack()
teste.push(1)
teste.push(2)
teste.pop()
