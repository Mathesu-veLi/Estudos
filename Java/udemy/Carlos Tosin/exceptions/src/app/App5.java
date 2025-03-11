package app;

import account.Account3;
import exceptions.InsufficientFundsException;

public class App5 {
  public static void main(String[] args) {
    Account3 a = new Account3("1234");
    a.deposit(500);
    System.out.println(a);

    try {
      a.withdraw(1000);
      System.out.println(a);
    } catch(InsufficientFundsException e) {
      System.out.println("pouco dinheiro");
    }
  }
}
