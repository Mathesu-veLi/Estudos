package terminal;

public class AppForEach {
    public static void main(String[] args) {
        Item
            .list()
            .stream()
            .forEach(System.out::println);
    }
}
