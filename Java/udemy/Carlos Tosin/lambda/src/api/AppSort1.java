package api;

import java.util.*;

public class AppSort1 {
    public static void main(String[] args) {
        var letters = new ArrayList<>(Arrays.asList('C', 'B', 'E', 'A'));
        System.out.println(letters);

        letters.sort(Character::compareTo);
        System.out.println(letters);

        letters.sort(Comparator.naturalOrder());
        System.out.println(letters);
    }
}
