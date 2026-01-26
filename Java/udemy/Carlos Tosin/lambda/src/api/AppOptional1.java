package api;

import java.util.Map;

public class AppOptional1 {
    public static void main(String[] args) {
        People people = new People(Map.of(1, "Paulo", 2, "Afonso", 3, "Levi"));

        var name = people.getNameById(6);
        if(name.isPresent()) {
            String upperName = name.get().toUpperCase();
            System.out.println(upperName);
        }
    }
}
