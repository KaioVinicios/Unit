class Fila {
    constructor() {
      this.itens = [];
    }
  
    enqueue(element) {
      this.itens.push(element);
    }
  
    dequeue() {
      return this.itens.shift();
    }
  
    front() {
      return this.itens[0];
    }
  
    isEmpty() {
      return this.itens.length === 0;
    }
  
    size() {
      return this.itens.length;
    }
  
    print() {
      console.log(this.itens.join(", "));
    }
  }
  
  // Q1
  const fila = new Fila();
  fila.enqueue("Carlos");
  fila.enqueue("Ana");
  fila.print(); 
  fila.dequeue();
  fila.print();
  
  // Q2
  const filaNomes = new Fila();
  filaNomes.enqueue("Carlos");
  filaNomes.enqueue("Ana");
  filaNomes.enqueue("Cícero");
  filaNomes.enqueue("Bia");
  filaNomes.enqueue("Diego");
  
  filaNomes.dequeue(); 
  console.log(filaNomes.front());
  console.log(filaNomes.size()); 
  
  // Q3
  const filaAtendimento = new Fila();
  filaAtendimento.enqueue("João");
  filaAtendimento.enqueue("Maria");
  filaAtendimento.enqueue("Pedro");
  filaAtendimento.enqueue("Paula");
  filaAtendimento.enqueue("Lucas");
  
  filaAtendimento.dequeue(); 
  console.log(`Ainda aguardam: ${filaAtendimento.size()}`); 
  console.log(`Próxima pessoa a ser atendida: ${filaAtendimento.front()}`); 
  
  // Q4
  function verificarFilaVazia(fila) {
    if (fila.isEmpty()) {
      console.log("A fila está vazia");
    } else {
      console.log("A fila tem elementos");
    }
  }
  verificarFilaVazia(filaAtendimento);
  
  // Q5
  function moverElementos(fila) {
    if (fila.size() >= 2) {
      const primeiro = fila.dequeue();
      const segundo = fila.dequeue();
      fila.enqueue(primeiro);
      fila.enqueue(segundo);
    }
  }
  const filaTest = new Fila();
  filaTest.enqueue("Carlos");
  filaTest.enqueue("Ana");
  filaTest.enqueue("Cícero");
  filaTest.enqueue("Bia");
  filaTest.enqueue("Diego");
  
  moverElementos(filaTest);
  filaTest.print();
  
  // Q6
  function ultimoElemento(fila) {
    return fila.itens[fila.size() - 1];
  }
  console.log(ultimoElemento(filaTest));