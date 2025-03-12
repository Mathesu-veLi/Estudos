package app;

import java.util.Objects;

public class App2 {
  public static void main(String[] args) {
    String s1 = "ABC";
    String s2 = "ABC";
    String s3 = "ABC";
    String s4 = s2;
    String s5 = s1;
    String s6 = new String("ABC");
    String s7 = s6.intern();

    printEquality(s1, s2);
    printEquality(s2, s3);
    printEquality(s3, s4);
    printEquality(s4, s5);
    printEquality(s5, s6);
    printEquality(s6, s7);
  }

  private static void printEquality(Object o1, Object o2) {
    System.out.println();
    System.out.println(o1 + " == " + o2 + " --> " + (o1 == o2));
    System.out.println(o1 + ".equals(" + o2 + ") --> " + (o1.equals(o2)));
  }


}
