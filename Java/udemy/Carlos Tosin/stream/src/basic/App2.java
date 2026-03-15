package basic;

import java.util.List;

public class App2 {
    public static void main(String[] args) {
        var people = List.of(new Person("Pedro", 15), new Person("Levi", 16), new Person("Joana", 30));

        people.stream()
            .map(Person::name)
            .map(String::toUpperCase)
            .sorted()
            .forEach(System.out::println);
    }

    record Person(String name, int age) { }
}
