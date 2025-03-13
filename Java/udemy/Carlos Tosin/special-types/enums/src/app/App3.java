package app;

import interfaces.Pet;

public class App3 {
  public static void main(String[] args) {
    Dog d = new Dog();
    talk(d);
    talk(MyPet.CAT);
  }

  private static void talk(Pet pet) {
    System.out.println(pet.talk());
  }
}
