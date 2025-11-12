package inout;

import java.io.*;

public class ByteTransferApp {
    public static void main(String[] args) throws IOException {
        try(
            /*InputStream in = new ByteArrayInputStream("Java = sensacional!".getBytes(StandardCharsets.UTF_8));
            OutputStream out = new FileOutputStream("examples/text")*/

            InputStream in = new FileInputStream("examples/text");
            OutputStream out = new ByteArrayOutputStream()
        ) {
            IOOperations.transfer(in, out);

            System.out.println(out);
        }
    }
}
