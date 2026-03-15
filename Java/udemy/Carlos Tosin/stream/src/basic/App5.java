package basic;

import java.util.List;

public class App5 {
    public static void main(String[] args) {
        var people = List.of(new Person("Pedro", 15), new Person("Levi", 16), new Person("Joana", 30));

        List<String> names = people.stream()
            .map(Person::name)
            .filter(n -> !n.startsWith("P"))
            .toList();

        System.out.println(names);
    }

    record Person(String name, int age) { }
}
