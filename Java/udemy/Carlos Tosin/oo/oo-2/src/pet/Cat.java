package pet;

public class Cat extends EarthPet {
  @Override
  public void talk() {
    super.talk("Miau");
  }

  @Override
  public void sleep(int time) {
    System.out.println("Cat sleeping");
  }
}
