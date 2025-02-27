public class EncapsulatedAccount {
  private String accountNumber;
  private String accountOwner;
  private double balance;

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

  void transfer (double amount, EncapsulatedAccount targetAccount) {
    this.withdraw(amount);
    targetAccount.deposit(amount);
  }

  void printBalance () {
    System.out.println("Balance: " + balance);
  }

  public String getAccountNumber () {
    return accountNumber;
  }

  public void setAccountNumber (String accountNumber) {
    this.accountNumber = accountNumber;
  }

  public String getAccountOwner () {
    return accountOwner;
  }

  public void setAccountOwner (String accountOwner) {
    this.accountOwner = accountOwner;
  }

  public void setBalance (double balance) {
    this.balance = balance;
  }

  public double getBalance () {
    return balance;
  }
}
