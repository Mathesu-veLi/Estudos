import entities.Contract;
import entities.Instalment;
import services.ContractService;
import services.PaypalService;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main (String[] args) {
    Locale.setDefault(Locale.US);
    Scanner sc = new Scanner(System.in);

    DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");

    System.out.println("Entre com os dados do contrato: ");
    System.out.print("Número: ");
    int number = sc.nextInt();
    System.out.print("Data (dd/MM/yyyy): ");
    LocalDate date = LocalDate.parse(sc.next(), fmt);
    System.out.print("Valor do contrato: ");
    double totalValue = sc.nextDouble();

    Contract obj = new Contract(number, date, totalValue);

    System.out.println("Entre com o número de parcelas: ");
    int n = sc.nextInt();

    ContractService contractService = new ContractService(new PaypalService());
    contractService.processContract(obj, n);

    System.out.println("Parcelas: ");
    for(Instalment instalment : obj.getInstallments())  {
      System.out.println(instalment);
    }
  }
}