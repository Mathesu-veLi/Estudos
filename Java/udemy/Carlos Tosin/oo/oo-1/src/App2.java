public class App2 {
  public static void main (String[] args) {
    Account a = new Account();

    a.deposit(100);
    a.deposit(200);

    a.withdraw(50);

    a.getBalance();
  }
}
