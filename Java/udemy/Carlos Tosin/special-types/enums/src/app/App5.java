package app;

import enums.Car;

public class App5 {
  public static void main(String[] args) {
    Car c = new Car(Car.Brand.BMW);
    System.out.println(c.getBrand());
  }
}
