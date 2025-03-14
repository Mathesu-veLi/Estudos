package format;

public class ExItems {
  public static void main(String[] args) {
    Item i1 = new Item("Item 1", 205, "EUR");
    Item i2 = new Item("Item 2", 562, "BRL");
    Item i3 = new Item("Item 3", 134, "USD");

    System.out.println(i1);
    System.out.println(i2);
    System.out.println(i3);
  }
}
