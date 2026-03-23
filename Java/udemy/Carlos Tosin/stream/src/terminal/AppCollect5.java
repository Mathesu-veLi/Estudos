package terminal;

import java.util.stream.Collectors;

public class AppCollect5 {
    public static void main(String[] args) {
        Item
            .list()
            .stream()
            .collect(Collectors.groupingBy(
                i -> i
                    .name()
                    .charAt(0), Collectors.summarizingDouble(Item::price)
            ))
            .forEach((k, v) -> System.out.println(k + " => " + v));
    }
}
