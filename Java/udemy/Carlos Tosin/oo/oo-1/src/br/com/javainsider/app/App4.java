package br.com.javainsider.app;

import br.com.javainsider.account.EncapsulatedAccount;

public class App4 {
  public static void main (String[] args) {
    var a = new EncapsulatedAccount("2345");
    a.deposit(1000);

    System.out.println(a.getAccountNumber());

    a.printBalance();
  }
}
