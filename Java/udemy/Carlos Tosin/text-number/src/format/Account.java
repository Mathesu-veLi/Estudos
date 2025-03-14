package format;

public class Account {
  String name;
  String number;
  double balance;

  public Account(String name, String number, double balance) {
    this.name = name;
    this.number = number;
    this.balance = balance;
  }

  public String getName() {
    return name;
  }

  public String getNumber() {
    return number;
  }

  public double getBalance() {
    return balance;
  }

  @Override
  public String toString() {
    return String.format("%-12s\t%-20s\t%10.2f", number, name, balance);
  }
}
