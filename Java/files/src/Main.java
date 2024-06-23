import java.io.*;
import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main (String[] args) {
    Locale.setDefault(Locale.US);
    Scanner sc = new Scanner(System.in);

    System.out.print("Path of file: ");
    String stringPath = sc.nextLine();
    File originalFile = new File(stringPath);

    copyProductsWithTotalPriceToSummary(originalFile);

    sc.close();
  }

  private static void copyProductsWithTotalPriceToSummary (File originalFile) {
    try (BufferedReader originalFileReader = new BufferedReader(new FileReader(originalFile))) {
      createFolderIfNoExist(originalFile.getParent());

      String summaryPath = String.format("%s/out/summary.csv", originalFile.getParent());
      writeInSummaryWithTotalPrice(summaryPath, originalFileReader);
    } catch (IOException e) {
      System.out.println("Error reading file: " + e.getMessage());
    }
  }

  private static void createFolderIfNoExist (String folderParent) {
    File folder = new File(folderParent + "/out");
    if (!folder.exists()) {
      folder.mkdir();
    }
  }

  private static void writeInSummaryWithTotalPrice (String summaryPath, BufferedReader originalFileReader) {
    try (BufferedWriter summaryWriter = new BufferedWriter(new FileWriter(summaryPath))) {
      String product = originalFileReader.readLine();

      while (product != null) {
        writeLn(summaryWriter, getProductWithTotalPrice(product));
        product = originalFileReader.readLine();
      }
    } catch (IOException e) {
      System.out.println("Error writing in summary: " + e.getMessage());
    }
  }

  private static void writeLn (BufferedWriter summary, String line) throws IOException {
    summary.write(line);
    summary.newLine();
  }

  private static String getProductWithTotalPrice (String product) {
    String[] productData = product.split(",");
    String name = productData[0];
    double price = Double.parseDouble(productData[1]);
    int quantity = Integer.parseInt(productData[2]);

    return String.format("%s,%.2f", name, getProductTotalPrice(price, quantity));
  }

  private static double getProductTotalPrice (double price, int quantity) {
    return price * (double) quantity;
  }
}
