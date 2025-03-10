package app;

import account.Account3;

public class App3 {
  public static void main(String[] args) {
    Account3 a = new Account3("1234");
    a.deposit(500);
    System.out.println(a);

    a.withdraw(-1000);

    System.out.println("Success!");
  }
}
