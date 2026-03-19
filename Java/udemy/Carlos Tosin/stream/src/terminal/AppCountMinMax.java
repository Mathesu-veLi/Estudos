package terminal;

public class AppCountMinMax {
    public static void main(String[] args) {
        long count = Item
            .list()
            .stream()
            .count();

        double max = Item
            .list()
            .stream()
            .mapToDouble(Item::price)
            .max()
            .orElseThrow();

        double min = Item
            .list()
            .stream()
            .mapToDouble(Item::price)
            .min()
            .orElseThrow();

        double average = Item
            .list()
            .stream()
            .mapToDouble(Item::price)
            .average()
            .orElseThrow();

        System.out.println(count);
        System.out.println(max);
        System.out.println(min);
        System.out.println(average);
    }
}
