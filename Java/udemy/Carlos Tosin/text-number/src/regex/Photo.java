package regex;

import java.util.Scanner;

public class Photo {
  private final int sequence;
  private final int yaer;
  private final String city;

  public Photo(int sequence, int yaer, String city) {
    this.sequence = sequence;
    this.yaer = yaer;
    this.city = city;
  }

  public int getSequence() {
    return sequence;
  }

  public int getYaer() {
    return yaer;
  }

  public String getCity() {
    return city;
  }

  @Override
  public String toString() {
    return "Photo{" + "sequence=" + sequence + ", yaer=" + yaer + ", city='" +
        city + '\'' + '}';
  }

  public static Photo createFromFileName(String filename) {
    Scanner scanner = new Scanner(filename);
    scanner.useDelimiter("[-.]");

    int sequential = Integer.parseInt(scanner.next().replaceAll("\\D", ""));
    int year = scanner.nextInt();
    String city = scanner.next().replaceAll("_", " ");

    return new Photo(sequential, year, city);
  }
}
