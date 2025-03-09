package app;

import generator.*;

public class App8 {
  public static void main(String[] args) {
    Generator randomGenerator = new SequenceGenerator();
    
    Person p1 = new Person(randomGenerator);
    System.out.println(p1.getId());

    Person p2 = new Person(randomGenerator);
    System.out.println(p2.getId());

    Person p3 = new Person(randomGenerator);
    System.out.println(p3.getId());
  }
}
