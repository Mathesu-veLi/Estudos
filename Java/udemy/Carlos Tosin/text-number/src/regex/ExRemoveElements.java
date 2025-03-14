package regex;

public class ExRemoveElements {
  public static void main(String[] args) {
    String text = "aawjnowpaowd33awd1aswd";
    System.out.println(text.replaceAll("\\D", ""));
  }
}
