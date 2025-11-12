package inout;

import java.io.*;
import java.nio.charset.StandardCharsets;

public class InputOutputStreamReaderWriterApp {
    private static final byte[] BYTES = {106, 97, 118, 97, 32, 114, 111, 99, 107, 115, 33, 32, 92, 111, 47};

    public static void main(String[] args) throws IOException {
        try(
            BufferedReader reader = new BufferedReader(
                new InputStreamReader(new ByteArrayInputStream(BYTES), StandardCharsets.UTF_8))
        ) {
            System.out.println(reader.readLine());
        }
    }
}
