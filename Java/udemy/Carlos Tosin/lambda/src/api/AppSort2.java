package api;

import java.util.Arrays;
import java.util.Comparator;

public class AppSort2 {
    public static void main(String[] args) {
        var people = Arrays.asList(new Person("Pedro", 25),
                                   new Person("Paulo", 30),
                                   new Person("Levi", 15),
                                   new Person("Maria", 23),
                                   new Person("Paulo", 32));

        people.sort(Comparator.comparing(Person::name).thenComparing(Person::age));
        //people.sort(Comparator.comparing(Person::age).reversed());

        people.forEach(p -> System.out.println(p.name + " - " + p.age));
    }

    record Person(String name, int age) {}

    ;
}
