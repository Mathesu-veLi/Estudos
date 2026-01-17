package interfaces;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class AppPredicate {
    public static void main(String[] args) {
        var list = List.of("1", "2", "3", "4", "5", "66");
        System.out.println(filter(list, s -> s.length() == 1));
    }

    private static List<String> filter(List<String> list, Predicate<String> predicate) {
        List<String> newList = new ArrayList<>();
        for(String e : list) {
            if(predicate.test(e)) {
                newList.add(e);
            }
        }
        return newList;
    }
}
