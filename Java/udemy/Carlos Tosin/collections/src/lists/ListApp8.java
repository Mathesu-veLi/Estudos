package lists;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class ListApp8 {
    public static void main(String[] args) {
        var people = new ArrayList<>(List.of(
                new Person("Maria", 45),
                new Person("Paulo", 36),
                new Person("Pedro", 40)
        ));

        //people.sort(new PersonComparator());
        //people.sort((o1, o2) -> o1.getName().compareTo(o2.getName()));
        people.sort(Comparator.comparing(Person::getName));

        for (var p : people) {
            System.out.printf("==> %s\n", p);
        }
    }
}
