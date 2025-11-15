package inout;

import java.io.*;
import java.nio.file.Path;

public class ReadAndReplace {
    public static void main(String[] args) throws IOException {
        try(
            var in = new BufferedReader(new FileReader("examples/data.in"));
            var out = new PrintWriter(Path.of("examples").resolve("data.out").toFile())
        ) {
            String line;
            while((line = in.readLine()) != null) {
                line = line.replace(".", ".\n");
                out.println(line);
            }
        }
    }
}
