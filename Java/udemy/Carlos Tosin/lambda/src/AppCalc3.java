import java.util.Locale;

public class AppCalc3 {
    public static void main(String[] args) {
        print(() -> "Hi!");
        print(() -> "Hello!");

        print(s -> s.toUpperCase(), "abc");
        print(s -> new StringBuilder(s).reverse().toString(), "abc");
    }

    private static void print(TextProvider textProvider) {
        System.out.println(textProvider.getText());
    }

    private static void print(TextTransformer textTransformer, String text) {
        System.out.println(textTransformer.transform(text));
    }
}
