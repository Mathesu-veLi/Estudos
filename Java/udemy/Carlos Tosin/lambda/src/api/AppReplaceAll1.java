package api;

import java.util.Arrays;

public class AppReplaceAll1 {
    public static void main(String[] args) {
        var numbers = Arrays.asList(0, 1, 2, 3, 4, 5);
        numbers.replaceAll(x -> x * 2);

        System.out.println(numbers);
    }
}
