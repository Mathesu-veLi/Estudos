package regex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class App4 {
  public static void main(String[] args) {
    String text = "e1j3e1p3wem1";
    String regex = "\\d";
    String replacement = "*";

    System.out.println(text.replaceAll(regex, replacement));
  }
}
