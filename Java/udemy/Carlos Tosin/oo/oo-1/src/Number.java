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

  public Number add (Number n1, Number n2) {
    return new Number(n1.getNumber() + n2.getNumber());
  }

  public static int getInstances () {
    return instances;
  }
}
