package sum;

import java.util.Scanner;

public class ExSum {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int number1 = readNumber(scanner);
    int number2 = readNumber(scanner);

    System.out.println("Resposta: " + (number1 + number2));
  }

  public static int readNumber(Scanner scanner) {
    System.out.print("Digite o número: ");

    try {
      return Integer.parseInt(scanner.nextLine());
    } catch(NumberFormatException e) {
      return 10;
    }
  }
}
