package app;

import pet2.*;

public class App7 {
  public static void main(String[] args) {
    Pet d = new Dog();
    Pet c = new Cat();

    feedPet(d);
    feedPet(c);
  }

  private static void feedPet(Pet p) {
    p.feed();
  }
}
