public class Tamagoshi {
    private String name;
    private boolean hunger;
    private String health;
    private int age;

    public void changeName(String name) {
        System.out.println("Nome" + name);
    }

    public boolean getHunger(){
        return hunger;
    }

    public void setHunger(boolean hunger){
        this.hunger = hunger;
    }

    public void showAge(int age) {
        System.out.println("Idade: " + age);
    }
}
