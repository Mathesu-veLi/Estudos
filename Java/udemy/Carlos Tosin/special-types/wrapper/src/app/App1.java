package app;

public class App1 {
  public static void main(String[] args) {
    int i = 10;
    Integer x = Integer.valueOf(i);

    int j = x.intValue();

    Double d = Double.valueOf(10.5);

    System.out.println(x);
    System.out.println(d);
  }
}
