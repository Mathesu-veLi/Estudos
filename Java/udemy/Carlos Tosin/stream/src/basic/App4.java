package basic;

import java.util.List;

public class App4 {
    public static void main(String[] args) {
        var people = List.of(new Person("Pedro", 15), new Person("Levi", 16), new Person("Joana", 30));

        int max = people.stream()
            .mapToInt(Person::age)
            .max()
            .orElse(0);

        int min = people.stream()
            .mapToInt(Person::age)
            .min()
            .orElse(0);

        double avg = people.stream()
            .mapToInt(Person::age)
            .average()
            .orElse(0);

        System.out.println(max);
        System.out.println(min);
        System.out.println(avg);
    }

    record Person(String name, int age) { }
}
