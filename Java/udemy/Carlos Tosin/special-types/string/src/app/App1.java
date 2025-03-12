package app;

public class App1 {
  public static void main(String[] args) {
    String s1 = "A";
    String s2 = "B";
    String s3 = "B";
    String s4 = new String("B");

    System.out.println(s2 == s3);
    System.out.println(s4 == s3);

    System.out.println(s2.equals(s3));
    System.out.println(s3.equals(s4));
  }
}
