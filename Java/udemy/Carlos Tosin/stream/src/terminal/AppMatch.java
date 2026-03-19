package terminal;

public class AppMatch {
    public static void main(String[] args) {
        boolean r1 = Item
            .list()
            .stream()
            .map(Item::name)
            .anyMatch(n -> n.startsWith("C"));
        System.out.println(r1);

        boolean r2 = Item
            .list()
            .stream()
            .map(Item::name)
            .allMatch(n -> n.startsWith("C"));
        System.out.println(r2);

        boolean r3 = Item
            .list()
            .stream()
            .map(Item::name)
            .noneMatch(n -> n.startsWith("C"));
        System.out.println(r3);
    }
}
