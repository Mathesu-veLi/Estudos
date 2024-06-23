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
      String line = originalFileReader.readLine();
      String summaryPath = String.format("%s/out/summary.csv", originalFile.getParent());

      createFolderIfNoExist(originalFile.getParent());

      try (BufferedWriter summary = new BufferedWriter(new FileWriter(summaryPath))) {
        while (line != null) {
          summary.write(line);
          summary.newLine();
          line = originalFileReader.readLine();
        }
      } catch (FileNotFoundException e) {
        System.out.println("Error: " + e.getMessage());
        System.out.println("2");
      }
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
      System.out.println("1");
    }

    sc.close();
  }

  private static void createFolderIfNoExist (String folderParent) {
    File folder = new File(folderParent + "/out");
    if (!folder.exists()) {
      folder.mkdir();
    }
  }
}
