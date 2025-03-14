package format;

public class App2 {
  public static void main(String[] args) {
    Account a1 = new Account("Pedro Almeida", "1244-34", 20);
    Account a2 = new Account("Julia Duarte", "873343-1242", 940);
    Account a3 = new Account("Denize Queiroz Guedes", "6265876-76", 230);
    Account a4 = new Account("Ana Beatriz Queiroz", "342742-2", 12300);

    System.out.println(a1);
    System.out.println(a2);
    System.out.println(a3);
    System.out.println(a4);
  }
}
