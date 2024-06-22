import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

public class Main {
  public static void main (String[] args) {
    File file = new File("/home/veli/Documentos/in.txt");
    Scanner sc = null;
    try {
      sc = new Scanner(file);
      while (sc.hasNextLine()) {
        System.out.println(sc.nextLine());
      }
    } catch(FileNotFoundException e) {
      System.out.println("Error: " + e.getMessage());
    } finally {
      sc.close();
    }
  }
}