import java.io.*;
import java.util.Scanner;

public class Main {
  public static void main (String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter a folder path: ");
    String strPath = sc.nextLine();

    File path = new File(strPath);
    File[] folders = path.listFiles(File::isDirectory);
    System.out.println("Folders: ");
    for (File folder : folders) {
      System.out.println(folder);
    }

    sc.close();
  }
}