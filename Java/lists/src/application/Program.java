package application;

import java.util.ArrayList;
import java.util.List;

public class Program {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();

        list.add("Maria");
        list.add("Alex");
        list.add("Bob");
        list.add("Anna");
        list.add(2, "Marco");

        for (String name : list) {
            System.out.println(name);
        }

        System.out.println("-------------");
        list.removeIf(x -> x.charAt(0) == 'M');


        for (String name : list) {
            System.out.println(name);
        }
        System.out.println("-----------");
        System.out.println("Index of Bob: " + list.indexOf("Bob"));
        System.out.println("Index of Marco: " + list.indexOf("Marco"));
        
    }
}
