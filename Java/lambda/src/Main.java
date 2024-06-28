import entites.Product;

import java.util.*;
import java.util.function.Predicate;

public class Main {
  public static void main (String[] args) {
    Locale.setDefault(Locale.US);
    List<Product> list = new ArrayList<>();

    list.add(new Product("Tv", 900.00));
    list.add(new Product("Mouse", 50.00));
    list.add(new Product("Tablet", 350.00));
    list.add(new Product("HD Case", 80.90));

    Predicate<Product> productPredicate = p -> p.getPrice() >= 100.0;

    list.removeIf(productPredicate);

    for (Product p : list) {
      System.out.println(p);
    }
  }
}