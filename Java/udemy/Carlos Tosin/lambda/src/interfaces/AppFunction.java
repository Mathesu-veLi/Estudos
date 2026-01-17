package interfaces;

import java.util.function.Function;

public class AppFunction {
    public static void main(String[] args) {
        Person p1 = new Person("Pedro", "Silva");
        System.out.println(map(p1, Person::firstName));
        System.out.println(map(p1, Person::lastName));
        System.out.println(map(p1, p -> p.firstName + " " + p.lastName));
    }

    private static String map(Person person, Function<Person, String> function) {
        return function.apply(person);
    }

    record Person(String firstName, String lastName) {}
}
