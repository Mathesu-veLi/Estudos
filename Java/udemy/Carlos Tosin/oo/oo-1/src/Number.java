public class Number {
  private static int instances;
  private int number;

  public Number (int number) {
    this.number = number;
    instances++;
  }

  public int getNumber () {
    return number;
  }

  public Number add(Number n1, Number n2) {
    return new Number(n1.getNumber() + n2.getNumber());
  }

  public static int getInstances () {
    return instances;
  }

  public static void main (String[] args) {
    var n1 = new Number(10);
    System.out.println(n1.getNumber());

    var n2 = new Number(5);
    var n3 = n2.add(n1, n2);
    System.out.println(n3.getNumber());

    System.out.println(Number.getInstances());
  }
}
