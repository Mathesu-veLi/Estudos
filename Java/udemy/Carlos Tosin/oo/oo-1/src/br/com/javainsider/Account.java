package br.com.javainsider;

public class Account {
  public String accountNumber;
  public String accountOwner;
  public double balance;

  boolean deposit(double amount) {
    if (amount > 0) {
      balance += amount;
      return true;
    }
    return false;
  }

  boolean deposit(String amount) {
    return deposit(Double.parseDouble(amount));
  }

  boolean withdraw(double amount) {
    if (balance >= amount && amount > 0) {
      balance -= amount;
      return true;
    }
    return false;
  }

  void transfer(double amount, Account targetAccount) {
    this.withdraw(amount);
    targetAccount.deposit(amount);
  }

  void getBalance() {
    System.out.println("Balance: " + balance);
  }
}
