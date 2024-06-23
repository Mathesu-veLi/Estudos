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

    try (BufferedReader originalFileReader = new BufferedReader(new FileReader(originalFile))) {
      createFolderIfNoExist(originalFile.getParent());

      String summaryPath = String.format("%s/out/summary.csv", originalFile.getParent());
      writeInSummary(summaryPath, originalFileReader);
    } catch (IOException e) {
      System.out.println("Error reading file: " + e.getMessage());
    }

    sc.close();
  }

  private static void createFolderIfNoExist (String folderParent) {
    File folder = new File(folderParent + "/out");
    if (!folder.exists()) {
      folder.mkdir();
    }
  }

  private static void writeInSummary (String summaryPath, BufferedReader originalFileReader) {
    try (BufferedWriter summary = new BufferedWriter(new FileWriter(summaryPath))) {
      String line = originalFileReader.readLine();

      while (line != null) {
        String[] productData = line.split(",");
        double totalPrice = Double.parseDouble(productData[1]) * Double.parseDouble(productData[2]);
        line = String.format("%s,%.2f", productData[0], totalPrice);

        writeLn(summary, line);
        line = originalFileReader.readLine();
      }
    } catch (IOException e) {
      System.out.println("Error writing in summary: " + e.getMessage());
    }
  }

  private static void writeLn (BufferedWriter summary, String line) throws IOException {
    summary.write(line);
    summary.newLine();
  }
}
