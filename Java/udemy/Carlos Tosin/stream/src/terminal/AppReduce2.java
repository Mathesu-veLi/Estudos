package terminal;

public class AppReduce2 {
    public static void main(String[] args) {
        var items = Item
            .list()
            .stream()
            .map(Item::name)
            .reduce("", (accum, s) -> accum + "," + s);

        System.out.println(items);
    }
}
