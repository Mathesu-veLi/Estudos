package api;

import java.util.Map;

public class AppOptional5 {
    public static void main(String[] args) {
        People people = new People(Map.of(1, "Paulo", 2, "Afonso", 3, "Levi"));

        people.getNameById(3)
            .filter(n -> n.startsWith("L"))
            .ifPresentOrElse(System.out::println, () -> System.out.println("Name does not start with L"));
    }
}
