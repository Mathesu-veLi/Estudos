package app;

import pet2.*;

public class App9 {
  public static void main(String[] args) {
    Pet p = new Fish();
    p.feed();

    /*Fish f = (Fish) p;
    f.feed();*/

    if(p instanceof Dog) {
      Dog d = (Dog) p;
      d.sit();
    } else {
      System.out.println("O tipo não é um Dog");
    }
  }
}
