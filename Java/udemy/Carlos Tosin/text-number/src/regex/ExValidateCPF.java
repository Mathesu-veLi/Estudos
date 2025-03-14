package regex;

public class ExValidateCPF {
  public static void main(String[] args) {
    System.out.println(validadeCPF("123.345.543-23"));
    System.out.println(validadeCPF("12334554323"));
    System.out.println(validadeCPF("123 345 543 23"));
    System.out.println(validadeCPF("123.345.543.23"));
  }

  private static boolean validadeCPF(String cpf) {
    return cpf.matches("\\d{3}([.\\s])?\\d{3}([.\\s])?\\d{3}([-\\s])?\\d{2}");
  }
}
