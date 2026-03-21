package terminal;

import java.util.stream.Collectors;

public class AppCollect1 {
    public static void main(String[] args) {
        var items1 = Item
            .list()
            .stream()
            .collect(Collectors.toList());

        var items2 = Item
            .list()
            .stream()
            .collect(Collectors.toUnmodifiableList());

        var items3 = Item
            .list()
            .stream()
            .collect(Collectors.toSet());

        var items4 = Item
            .list()
            .stream()
            .collect(Collectors.toUnmodifiableSet());

        System.out.println(items1);
        System.out.println(items2);
        System.out.println(items3);
        System.out.println(items4);
    }
}
