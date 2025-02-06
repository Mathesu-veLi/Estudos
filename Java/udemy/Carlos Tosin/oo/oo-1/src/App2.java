public class App2 {
  public static void main (String[] args) {
    Account a = new Account();


    if (!a.deposit(-100)) System.out.println("Ops, invalid deposit");
    a.getBalance();

    if (!a.deposit(200)) System.out.println("Ops, invalid deposit");
    a.getBalance();

    if (!a.withdraw(50)) System.out.println("Ops, invalid withdraw");
    a.getBalance();
  }
}
