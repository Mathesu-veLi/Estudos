public class App4 {
  public static void main (String[] args) {
    var a = new EncapsulatedAccount();
    a.deposit(1000);

    System.out.println(a.getAccountNumber());

    a.printBalance();
  }
}
