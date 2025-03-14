package format;

import java.text.NumberFormat;
import java.util.Currency;

public class App5 {
  public static void main(String[] args) {
    double n = 387656.21;

    NumberFormat nf = NumberFormat.getCurrencyInstance();

    nf.setGroupingUsed(false);
    nf.setMinimumFractionDigits(4);
    nf.setMinimumFractionDigits(4);
    nf.setCurrency(Currency.getInstance("EUR"));

    System.out.println(nf.format(n));
  }
}
