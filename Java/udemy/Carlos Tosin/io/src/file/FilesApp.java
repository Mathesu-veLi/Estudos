package file;

import java.nio.file.Files;
import java.nio.file.Path;

public class FilesApp {
    public static void main(String[] args) {
        Path file1 = Path.of("examples", "file1.txt");

        System.out.println(Files.exists(file1));
        System.out.println(Files.isDirectory(file1));
        System.out.println(Files.isRegularFile(file1));
    }
}
