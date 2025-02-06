public class Account {
  String accountNumber;
  String accountOwner;
  double balance;

  void deposit(double amount) {
    balance += amount;
  }

  void withdraw(double amount) {
    balance -= amount;
  }

  void getBalance() {
    System.out.println("Balance: " + balance);
  }
}
