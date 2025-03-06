public class ExNumber {
  public static void main (String[] args) {
    var n1 = new Number(10);
    System.out.println(n1.getNumber());

    var n2 = new Number(5);
    var n3 = n2.add(n1, n2);
    System.out.println(n3.getNumber());

    System.out.println(Number.getInstances());
  }
}
