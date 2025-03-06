package account;

public class SavingsAccount extends Account {
  private double rate;

  public SavingsAccount(String number) {
    super(number);
  }

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

  @Override
  public void print() {
    super.print();
    System.out.println("rate: " + rate);
  }
}
