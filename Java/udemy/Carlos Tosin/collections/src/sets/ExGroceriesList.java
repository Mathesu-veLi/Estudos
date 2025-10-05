package sets;

import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

public class ExGroceriesList {
    public static void main(String[] args) {
        List<String> items = new ArrayList<>();
        items.add("Bread");
        items.add("Ketchup");
        items.add("Potatoes");
        items.add("Ketchup");

        removeDuplications(items);

        for (var item : items) {
            System.out.println(item);
        }
    }

    public static void removeDuplications(List<String> items) {
        Set<String> set = new LinkedHashSet<>(items);
        items.clear();
        items.addAll(set);
    }
}
