package app;

public class App3 {
  public static void main(String[] args) {
    System.out.println(Integer.toBinaryString(15));
    System.out.println(Integer.toHexString(15));
    System.out.println(Integer.toOctalString(15));

    System.out.println(Integer.valueOf("11010", 2));
    System.out.println(Integer.valueOf("32fc", 16));

    System.out.println(Integer.decode("0x32fc"));
  }
}
