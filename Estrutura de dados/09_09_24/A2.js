// Q1
class FilaComPrioridade {
    constructor() {
      this.itens = [];
    }
  
    enqueue(element, priority) {
      const novoElemento = { element, priority };
      let adicionado = false;
  
      for (let i = 0; i < this.itens.length; i++) {
        if (this.itens[i].priority < novoElemento.priority) {
          this.itens.splice(i, 0, novoElemento);
          adicionado = true;
          break;
        }
      }
  
      if (!adicionado) {
        this.itens.push(novoElemento);
      }
    }
  
    dequeue() {
      if (this.isEmpty()) {
        return "Fila está vazia";
      }
      return this.itens.shift();
    }
  
    isEmpty() {
      return this.itens.length === 0;
    }
  
    print() {
      console.log(this.itens.map(item => `${item.element} - prioridade: ${item.priority}`).join(", "));
    }
}

const filaPrioridade = new FilaComPrioridade();
filaPrioridade.enqueue("Carlos", 1);
filaPrioridade.enqueue("Ana", 3);
filaPrioridade.enqueue("Bia", 2);
filaPrioridade.print();  
console.log(filaPrioridade.dequeue());
filaPrioridade.print();


// Q2
class Fila {
    constructor() {
      this.itens = [];
    }
  
    enqueue(element) {
      this.itens.push(element);
    }
  
    isEmpty() {
      return this.itens.length === 0;
    }
  
    print() {
      console.log(this.itens.join(", "));
    }
  }
  
  function isInOrder(fila) {
    for (let i = 0; i < fila.itens.length - 1; i++) {
      if (fila.itens[i] > fila.itens[i + 1]) {
        return false;
      }
    }
    return true;
}

const filaTest = new Fila();
filaTest.enqueue("A");
filaTest.enqueue("B");
filaTest.enqueue("C");
filaTest.enqueue("D");

console.log(isInOrder(filaTest));

filaTest.enqueue("Z");
console.log(isInOrder(filaTest));