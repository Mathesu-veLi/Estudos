public class Account {
  String accountNumber;
  String accountOwner;
  double balance;

  boolean deposit(double amount) {
    if (amount > 0) {
      balance += amount;
      return true;
    }
    return false;
  }

  boolean withdraw(double amount) {
    if (balance >= amount) {
      balance -= amount;
      return true;
    }
    return false;
  }

  void getBalance() {
    System.out.println("Balance: " + balance);
  }
}
