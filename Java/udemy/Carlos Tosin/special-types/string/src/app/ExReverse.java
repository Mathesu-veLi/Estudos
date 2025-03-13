package app;

import java.util.Scanner;

public class ExReverse {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("==> ");
    String text = scanner.nextLine();

    StringBuilder s = new StringBuilder(text).reverse();
    System.out.println("==> " + s);
  }
}
