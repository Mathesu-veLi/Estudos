package api;

import java.util.Map;

public class AppOptional6 {
    public static void main(String[] args) {
        People people = new People(Map.of(1, "Paulo", 2, "Afonso", 3, "Levi"));

        int count = people.getNameById(3).map(String::length).orElse(0);
        System.out.println(count);
    }
}
