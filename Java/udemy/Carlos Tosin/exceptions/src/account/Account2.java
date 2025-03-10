package account;

public class Account2 {
  private final String number;
  private double balance;

  public Account2(String number) {
    this.number = number;
  }

  public void deposit(double amount) {
    this.balance += amount;
  }

  public int withdraw(double amount) {
    if(amount < 0) {
      return -1;
    }

    if(balance - amount >= 0) {
      this.balance -= amount;
      return 1;
    }

    return -2;
  }

  @Override
  public String toString() {
    return "Account1{" + "number='" + number + '\'' + ", balance=" + balance +
        '}';
  }
}
