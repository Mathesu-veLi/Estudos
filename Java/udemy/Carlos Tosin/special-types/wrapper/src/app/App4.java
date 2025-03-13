package app;

public class App4 {
  public static void main(String[] args) {
    Integer i1 = new Integer(10);
    Integer i2 = new Integer(10);
    Integer i3 = 10;
    Integer i4 = 10;

    System.out.println(i1 == i2);
    System.out.println(i2 == i3);
    System.out.println(i3 == i4);

    System.out.println(i1.equals(i2));
    System.out.println(i2.equals(i3));
    System.out.println(i3.equals(i4));
  }
}
