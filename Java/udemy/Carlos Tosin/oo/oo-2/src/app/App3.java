package app;

import account.Account;

public class App3 {
  public static void main(String[] args) {
    Account a1 = new Account();
    a1.setNumber("1234");
    a1.setOwner("Pedro");
    a1.setBalance(1000);
    System.out.println(a1);
  }
}
