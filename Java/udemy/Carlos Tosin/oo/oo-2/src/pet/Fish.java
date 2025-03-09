package pet;

public class Fish extends WaterPet {
  @Override
  public void sleep(int time) {
    System.out.println("Fish sleeping");
  }
}
