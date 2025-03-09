package pet;

public abstract class EarthPet extends Pet {
  public void talk() {
    System.out.println("EarthPet talk");
  }

  public void talk(String talk) {
    System.out.println(talk);
  }

  public void walk() {
    System.out.println("EarthPet walk");
  }

  @Override
  public void sleep(int time) {
    System.out.println("EarthPet sleeping");
  }
}
