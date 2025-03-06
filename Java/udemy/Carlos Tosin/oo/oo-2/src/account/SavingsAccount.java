package account;

public class SavingsAccount extends Account {
  private double rate;

  public double getRate() {
    return rate;
  }

  public void setRate(double rate) {
    this.rate = rate;
  }

  @Override
  public void setBalance(double balance) {
    this.balance = balance * rate;
  }
}
