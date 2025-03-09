package pet;

public class Dog extends EarthPet {
  @Override
  public void talk() {
    super.talk("Au-au");
  }

  @Override
  public void sleep(int time) {
    System.out.println("Dog sleeping");
  }
}
