function Stack() {
    var items = []

    this.push = function(element) { 
        //adiciona um novo item a pilha
        items.push(element)
        
    }

    this.isEmpty = function() {
        //informar se a pilha esta vazia ou não
        return items.length === 0
    }
}

let teste = new Stack()
teste.push(1)
console.log(teste.isEmpty())