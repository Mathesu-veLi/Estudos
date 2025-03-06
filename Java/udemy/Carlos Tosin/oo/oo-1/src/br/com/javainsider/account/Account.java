package br.com.javainsider.account;

public class Account {
  public String accountNumber;
  public String accountOwner;
  public double balance;

  public boolean deposit (double amount) {
    if (amount > 0) {
      balance += amount;
      return true;
    }

    return false;
  }

  public boolean deposit (String amount) {
    return deposit(Double.parseDouble(amount));
  }

  public boolean withdraw (double amount) {
    if (balance >= amount && amount > 0) {
      balance -= amount;
      return true;
    }
    return false;
  }

  public void transfer (double amount, Account targetAccount) {
    this.withdraw(amount);
    targetAccount.deposit(amount);
  }

  public void getBalance () {
    System.out.println("Balance: " + balance);
  }
}
