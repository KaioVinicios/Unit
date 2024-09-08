// Esqueleto - Pilha
// vamos usar classe ( vamos trabalhar com objetos)
function Stack() {
    var items = []

    this.push = function(element) { 
        //adiciona um novo item a pilha
        items.push(element)
        
    }

    this.pop = function() {
        items.pop()
    }

    this.peek = function() {
        //devolve o elemento que está no topo d apilha
        return items[-1]        
    }

    this.isEmpty = function() {
        //informar se a pilha esta vazia ou não
        return items.length === 0
    }

    this.clear = function() {
        //limpa a pilha 
        items = []
    }

    this.size = function() {
        //informar o tamanho da pilha
        return items.length
   
    }

    this.print = function() {
        //imprime a pilha no console
        console.log(items)
    }
}

let teste = new Stack()
teste.push(2)
teste.print()