import entites.Product;

import java.util.*;

public class Main {
  public static void main (String[] args) {
    Locale.setDefault(Locale.US);
    List<Product> list = new ArrayList<>();

    list.add(new Product("Tv", 900.00));
    list.add(new Product("Mouse", 50.00));
    list.add(new Product("Tablet", 350.00));
    list.add(new Product("HD Case", 80.90));

    List<String> names = list.stream().map(p -> p.getName().toUpperCase()).toList();
    names.forEach(System.out::println);
  }
}