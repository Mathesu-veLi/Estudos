package terminal;

public class AppReduce {
    public static void main(String[] args) {
        double sum = Item
            .list()
            .stream()
            .mapToDouble(Item::price)
            .reduce(0, Double::sum);

        System.out.println(sum);
    }
}
