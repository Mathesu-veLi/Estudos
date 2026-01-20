package api;

import java.util.ArrayList;
import java.util.Arrays;

public class AppRemoveIf1 {
    public static void main(String[] args) {
        var letters = new ArrayList<>(Arrays.asList('A', 'b', 'C'));
        System.out.println(letters);

        letters.removeIf(Character::isLowerCase);
        System.out.println(letters);
    }
}
