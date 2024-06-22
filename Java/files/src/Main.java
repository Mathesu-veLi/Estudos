import java.io.*;

public class Main {
  public static void main (String[] args) {
    String path = "/home/veli/Documentos/out.txt";
    String[] lines = new String[] {"oi", "aaa"};

    try(BufferedWriter bw = new BufferedWriter(new FileWriter(path, true))) {
      for (String line : lines) {
        bw.write(line);
        bw.newLine();
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}