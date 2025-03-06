public class App7 {
  public static void main (String[] args) {
    var a1 = new IdGeneratedAccount("Pedro");
    System.out.println(a1.getAccountNumber());

    var a2 = new IdGeneratedAccount("Maria");
    System.out.println(a2.getAccountNumber());

    var a3 = new IdGeneratedAccount("Paulo");
    System.out.println(a3.getAccountNumber());
  }
}
