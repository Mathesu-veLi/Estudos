package basic;

import java.util.Comparator;
import java.util.List;

public class App3 {
    public static void main(String[] args) {
        var people = List.of(new Person("Pedro", 15), new Person("Levi", 16), new Person("Joana", 30));

        people.stream()
            .map(Person::age)
            .filter(age -> age >= 18)
            .sorted(Comparator.reverseOrder())
            .forEach(System.out::println);
    }

    record Person(String name, int age) { }
}
