public class Animal {
    public void emitirSom(){
        System.out.println("Esse animal faz um som.");
    }
}

class Gato extends Animal{
    @Override
    public void emitirSom() {
        System.out.println("O gato mia.");
    }

    public void arranharMoveis(){
        System.out.println("O gato arranha móveis.");
    }
}

class Cachorro extends Animal{
    @Override
    public void emitirSom() {
        System.out.println("O cachorro late.");
    }

    public void abanarRabo(){
        System.out.println("O cachorro abana o rabo.");
    }
}